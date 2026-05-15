import rclpy
from rclpy.node import Node

from sensor_msgs.msg import CompressedImage
from nav_msgs.msg import Odometry
from object_recognition_interfaces.srv import DetectObject, AddObject

from ultralytics import YOLO

import numpy as np
import cv2
import asyncio
from googletrans import Translator

import os
import shutil
import glob
from pathlib import Path


class ObjectRecognition(Node):

    def __init__(self):
        super().__init__('object_recognition_service')

        # =========================================================
        # RESOLVE PROJECT PATH (PORTABLE)
        # =========================================================
        base_path = Path(__file__).resolve().parent

        project_root = base_path
        while project_root.name != "src" and project_root.parent != project_root:
            project_root = project_root.parent

        model_dir = project_root / "object_recognition" / "models"
        model_dir.mkdir(parents=True, exist_ok=True)

        model_path = model_dir / "yolov8n.pt"

        self.get_logger().info(f"YOLO model path: {model_path}")

        # =========================================================
        # AUTO-DOWNLOAD IF MISSING
        # =========================================================
        if not model_path.exists():
            self.get_logger().warn("YOLO model not found. Downloading...")

            # Trigger Ultralytics download
            YOLO("yolov8n.pt")

            # Try to find cached file
            cache_files = glob.glob(str(Path.home() / ".cache/ultralytics/yolov8n.pt"))

            if cache_files:
                shutil.copy(cache_files[0], model_path)
                self.get_logger().info("YOLO downloaded and stored in project folder")
            else:
                self.get_logger().error("YOLO download failed")
                raise FileNotFoundError("yolov8n.pt could not be downloaded")

        # =========================================================
        # LOAD YOLO MODEL
        # =========================================================
        self.model = YOLO(str(model_path))
        self.get_logger().info("YOLO model loaded successfully")

        # =========================================================
        # CONFIDENCE
        # =========================================================
        self.conf_threshold = 0.3

        # =========================================================
        # STATE
        # =========================================================
        self.latest_frame = None
        self.odom = None

        # =========================================================
        # TRANSLATOR
        # =========================================================
        self.translator = Translator()
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
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        self.latest_frame = frame

    # -------------------------------------------------
    def translate(self, text):

        if text in self.translation_cache:
            return self.translation_cache[text]

        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            result = loop.run_until_complete(
                self.translator.translate(text, src='en', dest='es')
            )

            translated = result.text
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

        frame = self.latest_frame
        h, w, _ = frame.shape

        frame = frame[:, :w // 2]

        results = self.model(frame, verbose=False)

        center_x = (w // 2) / 2

        best = None
        best_score = 1e9

        for r in results:
            for box in r.boxes:

                cls = int(box.cls[0])
                conf = float(box.conf[0])

                if conf < self.conf_threshold:
                    continue

                x1, y1, x2, y2 = box.xyxy[0]
                obj_x = (x1 + x2) / 2

                score = abs(obj_x - center_x)

                if score < best_score:

                    best_score = score

                    label_en = self.model.names[cls]
                    label_es = self.translate(label_en)

                    best = {
                        "name": label_es,
                        "conf": conf
                    }

        if best is None:
            response.success = False
            self.get_logger().info("No object detected")
            return response

        self.get_logger().info(
            f"Object detected: {best['name']} (conf={best['conf']:.2f})"
        )

        self.call_add_object(best["name"])

        response.object = best["name"]
        response.confidence = best["conf"]
        response.success = True

        return response

    # -------------------------------------------------
    def call_add_object(self, name):

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