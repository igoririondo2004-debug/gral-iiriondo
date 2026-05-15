import queue
import time
import numpy as np
import sounddevice as sd
import webrtcvad

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import torch

from faster_whisper import WhisperModel

# =====================================================
# CONFIG
# =====================================================
SAMPLE_RATE = 16000

FRAME_DURATION = 30  # ms
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION / 1000)

SILENCE_LIMIT = 1.0  # seconds of silence before transcription

# minimum speech required before transcribing
MIN_SPEECH_FRAMES = 15

MODEL_NAME = "medium"

# =====================================================
# NODE
# =====================================================
class FasterWhisperNode(Node):

    def __init__(self):
        super().__init__("whisper_medium_node")

        # =================================================
        # ROS2 PUB
        # =================================================
        self.publisher_ = self.create_publisher(
            String,
            "speech_text",
            10
        )

        # =================================================
        # DEVICE
        # =================================================
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.get_logger().info(f"Device: {self.device}")

        # =================================================
        # MODEL
        # =================================================
        self.get_logger().info("Loading Faster-Whisper model...")

        self.model = WhisperModel(
            MODEL_NAME,
            device=self.device,
            compute_type="float16" if self.device == "cuda" else "int8"
        )

        self.get_logger().info("Model loaded")

        # =================================================
        # VAD
        # =================================================
        self.vad = webrtcvad.Vad(2)

        # =================================================
        # AUDIO STATE
        # =================================================
        self.q = queue.Queue()

        self.buffer = []

        self.speech_active = False

        self.speech_frames = 0

        self.last_voice_time = time.time()

        # =================================================
        # MIC STREAM
        # =================================================
        self.stream = sd.RawInputStream(
            samplerate=SAMPLE_RATE,
            blocksize=FRAME_SIZE,
            dtype="int16",
            channels=1,
            callback=self.audio_callback
        )

        self.stream.start()

        # =================================================
        # TIMER
        # =================================================
        self.timer = self.create_timer(
            0.05,
            self.process_audio
        )

        self.get_logger().info("Faster-Whisper node started")

    # =================================================
    # AUDIO CALLBACK
    # =================================================
    def audio_callback(self, indata, frames, time_info, status):

        if status:
            self.get_logger().warn(str(status))

        self.q.put(bytes(indata))

    # =================================================
    # VAD CHECK
    # =================================================
    def is_speech(self, frame_bytes):

        try:
            return self.vad.is_speech(
                frame_bytes,
                SAMPLE_RATE
            )

        except:
            return False

    # =================================================
    # PROCESS AUDIO
    # =================================================
    def process_audio(self):

        while not self.q.empty():

            frame = self.q.get()

            speech = self.is_speech(frame)

            now = time.time()

            # =============================================
            # SPEECH DETECTED
            # =============================================
            if speech:

                self.buffer.append(frame)

                self.speech_frames += 1

                self.speech_active = True

                self.last_voice_time = now

            # =============================================
            # SILENCE
            # =============================================
            else:

                # keep short silence inside phrase
                if self.speech_active:
                    self.buffer.append(frame)

                # enough silence -> transcribe
                if (
                    self.speech_active and
                    self.speech_frames >= MIN_SPEECH_FRAMES and
                    (now - self.last_voice_time > SILENCE_LIMIT)
                ):

                    self.transcribe()

                    # reset state
                    self.buffer = []

                    self.speech_frames = 0

                    self.speech_active = False

                # reset tiny noises
                elif (
                    self.speech_active and
                    self.speech_frames < MIN_SPEECH_FRAMES and
                    (now - self.last_voice_time > SILENCE_LIMIT)
                ):

                    # self.get_logger().info("Ignored short noise")

                    self.buffer = []

                    self.speech_frames = 0

                    self.speech_active = False

    # =================================================
    # TRANSCRIBE
    # =================================================
    def transcribe(self):

        if len(self.buffer) == 0:
            return

        self.get_logger().info("Transcribing...")

        audio_bytes = b"".join(self.buffer)

        audio = (
            np.frombuffer(audio_bytes, np.int16)
            .astype(np.float32)
            / 32768.0
        )

        segments, info = self.model.transcribe(
            audio,
            language="es",
            beam_size=1
        )

        text = " ".join(
            [segment.text for segment in segments]
        ).strip()

        if text:

            msg = String()

            msg.data = text

            self.publisher_.publish(msg)

            self.get_logger().info(f"[ASR] {text}")

        else:
            self.get_logger().info("Empty transcription")

# =====================================================
# MAIN
# =====================================================
def main(args=None):

    rclpy.init(args=args)

    node = FasterWhisperNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()