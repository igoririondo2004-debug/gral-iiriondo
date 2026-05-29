import rclpy
from rclpy.node import Node

from sensor_msgs.msg import CompressedImage
from nav_msgs.msg import Odometry
from object_recognition_interfaces.srv import DetectObject, AddObject

import numpy as np
import cv2
import asyncio
from deep_translator import GoogleTranslator

import os
import shutil
import glob
from pathlib import Path

# ============================
# ViT / PyTorch imports
# ============================
import torch
import timm
import torchvision.transforms as T
from PIL import Image
import urllib.request


class ObjectRecognition(Node):

    def __init__(self):
        super().__init__('object_recognition_service')

        # =========================================================
        # STATE
        # =========================================================
        self.latest_frame = None
        self.odom = None

        # =========================================================
        # CONFIDENCE
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
        # VIT MODEL (ImageNet-1K)
        # =========================================================
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.model = timm.create_model(
            "vit_base_patch16_224",
            pretrained=True
        )
        self.model.eval()
        self.model.to(self.device)

        # preprocessing
        self.transform = T.Compose([
            T.ToPILImage(),
            T.Resize((224, 224)),
            T.ToTensor(),
            T.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

        # =========================================================
        # IMAGENET LABELS
        # =========================================================
        labels_path = str(Path.home() / ".imagenet_labels.txt")

        if not os.path.exists(labels_path):
            self.get_logger().info("Downloading ImageNet labels...")

            fallback_url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"

            try:
                urllib.request.urlretrieve(fallback_url, labels_path)
            except Exception as e:
                self.get_logger().error(f"Failed to download labels: {e}")
                raise RuntimeError("Cannot load ImageNet labels")

        with open(labels_path, "r") as f:
            self.labels = [line.strip() for line in f.readlines()]

        # =========================================================
        # SERVICE SERVER
        # =========================================================
        self.create_service(
            DetectObject,
            '/object_recognition/detect_object',
            self.detect_cb
        )

        self.get_logger().info("ViT Object Recognition READY")

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
            translated = GoogleTranslator(source='en', target='es').translate(text)
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

        # =====================================================
        # PREPROCESS IMAGE FOR VIT
        # =====================================================
        img = self.transform(frame).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(img)
            probs = torch.nn.functional.softmax(outputs[0], dim=0)

            conf, cls = torch.max(probs, dim=0)

        conf = float(conf.item())
        cls = int(cls.item())

        # =====================================================
        # PRINT RAW PREDICTION (BEFORE CONFIDENCE FILTER)
        # =====================================================
        label_en_raw = self.labels[cls]
        self.get_logger().info(
            f"[RAW PREDICTION] {label_en_raw} (conf={conf:.2f})"
        )

        # =====================================================
        # CONFIDENCE FILTER
        # =====================================================
        if conf < self.conf_threshold:
            self.get_logger().info("No confident prediction")
            response.success = False
            return response

        # =====================================================
        # LABEL (FINAL)
        # =====================================================
        label_en = label_en_raw
        label_es = self.translate(label_en)

        self.get_logger().info(
            f"ViT detected: {label_es} (conf={conf:.2f})"
        )

        # =====================================================
        # ADD TO MAP
        # =====================================================
        self.call_add_object(label_es)

        response.object = label_es
        response.confidence = conf
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