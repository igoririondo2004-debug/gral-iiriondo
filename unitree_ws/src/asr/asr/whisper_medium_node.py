#!/usr/bin/env python3
import queue
import time
import numpy as np
import sounddevice as sd

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import torch
import whisper

# =====================================================
# CONFIG
# =====================================================
SAMPLE_RATE = 16000
FRAME_DURATION = 30  # ms
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION / 1000)
SILENCE_LIMIT = 1.0  # seconds of silence before transcription
MIN_SPEECH_FRAMES = 15

MODEL_NAME = "medium"

# =====================================================
# NODE
# =====================================================
class WhisperPyTorchNode(Node):

    def __init__(self):
        super().__init__("whisper_medium_node")

        # Publisher for transcribed text
        self.publisher_ = self.create_publisher(String, "speech_text", 10)

        # Device selection
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.get_logger().info(f"Using device: {self.device}")

        # Load Whisper model
        self.get_logger().info(f"Loading Whisper model '{MODEL_NAME}'...")
        self.model = whisper.load_model(MODEL_NAME, device=self.device)
        self.get_logger().info("Model loaded successfully")

        # VAD and audio buffering
        self.q = queue.Queue()
        self.buffer = []
        self.speech_active = False
        self.speech_frames = 0
        self.last_voice_time = time.time()

        # Audio stream
        self.stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            blocksize=FRAME_SIZE,
            channels=1,
            dtype="float32",
            callback=self.audio_callback
        )
        self.stream.start()

        # Timer to process audio periodically
        self.timer = self.create_timer(0.05, self.process_audio)
        self.get_logger().info("Whisper PyTorch node started")

    # Audio callback: put frames in queue
    def audio_callback(self, indata, frames, time_info, status):
        if status:
            self.get_logger().warn(str(status))
        self.q.put(indata.copy())

    # Simple energy-based voice activity detection
    def is_speech(self, frame):
        energy = np.mean(frame ** 2)
        return energy > 0.0003

    # Process queued audio frames
    def process_audio(self):
        while not self.q.empty():
            frame = self.q.get()
            speech = self.is_speech(frame)
            now = time.time()

            if speech:
                self.buffer.append(frame)
                self.speech_frames += 1
                self.speech_active = True
                self.last_voice_time = now
            else:
                if self.speech_active:
                    self.buffer.append(frame)

                if self.speech_active and self.speech_frames >= MIN_SPEECH_FRAMES and (now - self.last_voice_time > SILENCE_LIMIT):
                    self.transcribe()
                    self.buffer = []
                    self.speech_frames = 0
                    self.speech_active = False
                elif self.speech_active and self.speech_frames < MIN_SPEECH_FRAMES and (now - self.last_voice_time > SILENCE_LIMIT):
                    self.buffer = []
                    self.speech_frames = 0
                    self.speech_active = False

    # Transcribe buffered audio
    def transcribe(self):
        if not self.buffer:
            return

        try:
            audio = np.concatenate(self.buffer, axis=0).flatten()
            # Whisper expects float32 in [-1, 1]
            audio = audio.astype(np.float32)

            self.get_logger().info("Transcribing audio...")
            result = self.model.transcribe(audio, language="es")

            text = result.get("text", "").strip()
            if text:
                msg = String()
                msg.data = text
                self.publisher_.publish(msg)
                self.get_logger().info(f"[ASR] {text}")
            else:
                self.get_logger().info("Empty transcription")
        except Exception as e:
            self.get_logger().error(f"Transcription failed: {str(e)}")

# =====================================================
# MAIN
# =====================================================
def main(args=None):
    rclpy.init(args=args)
    node = WhisperPyTorchNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Whisper node...")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()