import os
import queue
import json
import sounddevice as sd
import urllib.request
import zipfile

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from vosk import Model, KaldiRecognizer


MODEL_URLS = {
    "en": "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip",
    "es": "https://alphacephei.com/vosk/models/vosk-model-small-es-0.42.zip",
    "fr": "https://alphacephei.com/vosk/models/vosk-model-small-fr-0.22.zip",
}


class VoskNode(Node):

    def __init__(self):
        super().__init__('vosk_asr_node')

        self.declare_parameter('language', 'en')
        self.declare_parameter('sample_rate', 16000)

        language = self.get_parameter('language').value
        sample_rate = self.get_parameter('sample_rate').value

        self.model_dir = os.path.expanduser("~/.vosk_models")

        os.makedirs(self.model_dir, exist_ok=True)

        model_path = self.ensure_model(language)

        self.get_logger().info(f"Using model: {language}")

        self.publisher_ = self.create_publisher(String, 'speech_text', 10)

        self.q = queue.Queue(maxsize=50)

        self.model = Model(model_path)
        self.rec = KaldiRecognizer(self.model, sample_rate)

        self.stream = sd.RawInputStream(
            samplerate=sample_rate,
            blocksize=8000,
            dtype='int16',
            channels=1,
            callback=self.audio_callback
        )
        self.stream.start()

        self.timer = self.create_timer(0.1, self.process_audio)

    # -------------------------
    # AUTO DOWNLOAD + LOAD
    # -------------------------
    def ensure_model(self, language):
        url = MODEL_URLS.get(language)

        if url is None:
            self.get_logger().warn(f"Unknown language {language}, falling back to EN")
            language = "en"
            url = MODEL_URLS["en"]

        model_name = url.split("/")[-1].replace(".zip", "")
        model_path = os.path.join(self.model_dir, model_name)

        # already exists
        if os.path.exists(model_path):
            return model_path

        self.get_logger().info(f"Downloading Vosk model for {language}...")

        zip_path = os.path.join(self.model_dir, model_name + ".zip")

        urllib.request.urlretrieve(url, zip_path)

        self.get_logger().info("Extracting model...")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.model_dir)

        os.remove(zip_path)

        return model_path

    # -------------------------
    # AUDIO
    # -------------------------
    def audio_callback(self, indata, frames, time, status):
        if status:
            self.get_logger().warn(str(status))

        try:
            self.q.put_nowait(bytes(indata))
        except queue.Full:
            pass

    def process_audio(self):
        while not self.q.empty():
            data = self.q.get()

            if self.rec.AcceptWaveform(data):
                result = json.loads(self.rec.Result())
                text = result.get("text", "").strip()

                if text:
                    msg = String()
                    msg.data = text
                    self.publisher_.publish(msg)
                    self.get_logger().info(f"[ASR] {text}")


def main(args=None):
    rclpy.init(args=args)
    node = VoskNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()