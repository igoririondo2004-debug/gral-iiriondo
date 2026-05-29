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

        model_path = model_dir / "yolo11n.pt"

        self.get_logger().info(f"YOLO model path: {model_path}")

        # =========================================================
        # DOWNLOAD IF NEEDED
        # =========================================================
        if not model_path.exists():
            self.get_logger().warn("YOLO model not found. Downloading...")

            YOLO("yolo11n.pt")

            cache_files = glob.glob(str(Path.home() / ".cache/ultralytics/yolo11n.pt"))

            if cache_files:
                shutil.copy(cache_files[0], model_path)
                self.get_logger().info("YOLO downloaded successfully")
            else:
                self.get_logger().error("YOLO download failed")
                raise FileNotFoundError("yolo11n.pt not found")

        # =========================================================
        # LOAD MODEL
        # =========================================================
        self.model = YOLO(str(model_path))
        self.get_logger().info("YOLO model loaded")

        # =========================================================
        # CONFIDENCE
        # =========================================================
        self.conf_threshold = 0.4

        # =========================================================
        # STATE
        # =========================================================
        self.latest_frame = None
        self.odom = None

        # =========================================================
        # TRANSLATOR (FIXED)
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
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        self.latest_frame = frame

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

        frame = self.latest_frame
        h, w, _ = frame.shape

        # keep only left half (your original logic)
        frame = frame[:, :w // 2]

        results = self.model(frame, verbose=False)

        self.get_logger().info("----- YOLO RAW OUTPUT -----")

        best_conf = -1.0
        best_cls = None

        # iterate detections
        for r in results:

            if r.boxes is None or len(r.boxes) == 0:
                continue

            for box in r.boxes:

                cls = int(box.cls[0])
                conf = float(box.conf[0])

                x1, y1, x2, y2 = box.xyxy[0]

                label_en = self.model.names[cls]

                # log all detections
                self.get_logger().info(
                    f"[RAW] {label_en} | conf={conf:.3f} | "
                    f"box=({x1:.0f},{y1:.0f},{x2:.0f},{y2:.0f})"
                )

                # filter weak detections
                if conf < self.conf_threshold:
                    continue

                # keep best only
                if conf > best_conf:
                    best_conf = conf
                    best_cls = cls

        # -----------------------------
        # RETURN ONLY BEST DETECTION
        # -----------------------------
        if best_cls is not None:

            label_en = self.model.names[best_cls]
            label_es = self.translate(label_en)

            response.success = True
            response.name = label_es
            response.conf = best_conf

        else:
            response.success = False

        return response

    def detect_cb(self, request, response):

        if self.latest_frame is None or self.odom is None:
            response.success = False
            return response

        frame = self.latest_frame
        h, w, _ = frame.shape

        # keep only left half (your original logic)
        frame = frame[:, :w // 2]

        results = self.model(frame, verbose=False)

        self.get_logger().info("----- YOLO RAW OUTPUT -----")

        best_conf = -1.0
        best_box = None
        best_cls = None

        save_dir = "/home/tknika/gral-iiriondo/unitree_ws/src/object_recognition/test_pictures"
        os.makedirs(save_dir, exist_ok=True)

        # YOLO usually returns one result per image
        for r in results:

            if r.boxes is None or len(r.boxes) == 0:
                continue

            for box in r.boxes:

                cls = int(box.cls[0])
                conf = float(box.conf[0])

                x1, y1, x2, y2 = box.xyxy[0]

                label_en = self.model.names[cls]

                # RAW LOG (still prints everything)
                self.get_logger().info(
                    f"[RAW] {label_en} | conf={conf:.3f} | "
                    f"box=({x1:.0f},{y1:.0f},{x2:.0f},{y2:.0f})"
                )

                # skip weak detections
                if conf < self.conf_threshold:
                    continue

                # keep ONLY best
                if conf > best_conf:
                    best_conf = conf
                    best_box = (x1, y1, x2, y2)
                    best_cls = cls

        # -----------------------------
        # SAVE ONLY ONE IMAGE (BEST)
        # -----------------------------
        if best_box is not None:

            x1, y1, x2, y2 = best_box

            label_en = self.model.names[best_cls]
            label_es = self.translate(label_en)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

            filename = f"{label_en}_{best_conf:.2f}_{timestamp}.jpg"
            filepath = os.path.join(save_dir, filename)

            annotated = frame.copy()

            cv2.rectangle(
                annotated,
                (int(x1), int(y1)),
                (int(x2), int(y2)),
                (0, 255, 0),
                2
            )

            cv2.putText(
                annotated,
                f"{label_en} {best_conf:.2f}",
                (int(x1), int(y1) - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

            cv2.imwrite(filepath, annotated)

            best = {
                "name": label_es,
                "conf": best_conf
            }

            response.success = True
            response.object = best["name"]
            response.confidence = best["conf"]

        else:
            response.success = False

        return response

        if best is None:
            self.get_logger().info("No object selected after filtering")
            response.success = False
            return response

        self.get_logger().info(
            f"SELECTED: {best['name']} (conf={best['conf']:.2f})"
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