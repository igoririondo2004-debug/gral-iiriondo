import rclpy
from rclpy.node import Node

from sensor_msgs.msg import CompressedImage
from nav_msgs.msg import Odometry
from object_recognition_interfaces.srv import DetectObject, AddObject

from ultralytics import YOLO

import numpy as np
import cv2
import os
import shutil
import glob
from pathlib import Path
from deep_translator import GoogleTranslator
from datetime import datetime


class ObjectRecognition(Node):

    def __init__(self):
        super().__init__('object_recognition_service')

        # =========================================================
        # MODEL PATH
        # =========================================================
        base_path = Path(__file__).resolve().parent

        project_root = base_path
        while project_root.name != "src" and project_root.parent != project_root:
            project_root = project_root.parent

        model_dir = project_root / "object_recognition" / "models"
        model_dir.mkdir(parents=True, exist_ok=True)

        model_path = model_dir / "yolov8n-cls.pt"

        self.get_logger().info(f"YOLO model path: {model_path}")

        # =========================================================
        # LOAD MODEL (ROBUST VERSION)
        # =========================================================

        # If you already have a local copy → use it
        if model_path.exists():
            self.get_logger().info("Loading YOLO from local model path")
            self.model = YOLO(str(model_path))

        else:
            self.get_logger().warn("Local model not found. Loading via Ultralytics (auto-download)")

            # This will auto-download if needed and cache internally
            self.model = YOLO("yolov8n-cls.pt")

            # Optional: save a local copy for future offline use
            try:
                self.model.save(str(model_path))
                self.get_logger().info("Saved YOLO model to local workspace")
            except Exception as e:
                self.get_logger().warn(f"Could not save local copy: {e}")

        self.get_logger().info("YOLO model loaded successfully")

        # =========================================================
        # STATE
        # =========================================================
        self.latest_frame = None
        self.odom = None

        # =========================================================
        # CONFIDENCE THRESHOLD
        # =========================================================
        self.conf_threshold = 0.3

        # =========================================================
        # TRANSLATOR
        # =========================================================
        self.translator = GoogleTranslator(source='en', target='es')
        self.translation_cache = {}

        # =========================================================
        # SUBSCRIPTIONS
        # =========================================================
        self.create_subscription(
            CompressedImage,
            '/camera/head/front/image_raw/compressed',
            self.image_cb,
            10
        )

        self.create_subscription(
            Odometry,
            '/odom',
            self.odom_cb,
            10
        )

        # =========================================================
        # SERVICE CLIENT
        # =========================================================
        self.add_cli = self.create_client(AddObject, '/aruco/add_marker')
        while not self.add_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for /aruco/add_marker service...")

        # =========================================================
        # SERVICE SERVER
        # =========================================================
        self.create_service(
            DetectObject,
            '/object_recognition/detect_object',
            self.detect_cb
        )

        self.get_logger().info("Detect Object Service READY")

    # -------------------------------------------------
    def odom_cb(self, msg):
        self.odom = msg.pose.pose.position

    # -------------------------------------------------
    def image_cb(self, msg):
        np_arr = np.frombuffer(msg.data, np.uint8)
        self.latest_frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # -------------------------------------------------
    def translate(self, text):
        if text in self.translation_cache:
            return self.translation_cache[text]
        try:
            translated = self.translator.translate(text)
            self.translation_cache[text] = translated
            return translated
        except Exception as e:
            self.get_logger().warn(f"Translate error: {e}")
            return text

    # -------------------------------------------------
    def detect_cb(self, request, response):
        if self.latest_frame is None or self.odom is None:
            response.success = False
            return response

        # =====================================================
        # GET FRAME (LEFT HALF)
        # =====================================================
        frame = self.latest_frame
        h, w, _ = frame.shape
        frame = frame[:, :w // 2]

        # =====================================================
        # YOLO CLASSIFICATION
        # =====================================================
        results = self.model(frame, verbose=False)[0]
        probs = results.probs

        if probs is None:
            self.get_logger().info("No classification output")
            response.success = False
            return response

        top1 = int(probs.top1)
        conf = float(probs.top1conf)
        label_en = self.model.names[top1]

        # =====================================================
        # PRINT RAW PREDICTION BEFORE FILTER
        # =====================================================
        self.get_logger().info(f"[RAW PREDICTION] {label_en} (conf={conf:.2f})")

        # =====================================================
        # FILTER BY CONFIDENCE
        # =====================================================
        if conf < self.conf_threshold:
            self.get_logger().info(
                f"Prediction confidence too low ({conf:.2f} < {self.conf_threshold}), ignoring"
            )
            response.success = False
            return response

        label_es = self.translate(label_en)

        self.get_logger().info(
            f"CLASSIFICATION: {label_en} -> {label_es} (conf={conf:.2f})"
        )

        # =====================================================
        # ADD OBJECT TO MAP
        # =====================================================
        self.call_add_object(label_es)

        # =====================================================
        # RESPONSE
        # =====================================================
        response.object = label_es
        response.confidence = conf
        response.success = True

        return response

    # -------------------------------------------------
    def call_add_object(self, name):
        if self.odom is None:
            self.get_logger().warn("No odometry, cannot add object to map")
            return

        req = AddObject.Request()
        req.name = name
        req.x = float(self.odom.x)
        req.y = float(self.odom.y)
        req.z = 0.0

        future = self.add_cli.call_async(req)
        future.add_done_callback(self.add_response)

    # -------------------------------------------------
    def add_response(self, future):
        try:
            res = future.result()
            if res.success:
                self.get_logger().info("Object added to map")
            else:
                self.get_logger().warn("Mapper rejected object")
        except Exception as e:
            self.get_logger().error(f"AddObject error: {e}")


# -------------------------------------------------
def main():
    rclpy.init()
    node = ObjectRecognition()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()