import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from sensor_msgs.msg import CompressedImage, CameraInfo, Image
from cv_bridge import CvBridge

import numpy as np
import cv2
import json

from aruco_markers_msgs.msg import MarkerArray, Marker


class ArucoDetector(Node):

    def __init__(self):
        super().__init__('aruco_detector_node')

        # -------------------------
        # PARAMETERS
        # -------------------------
        self.declare_parameter("marker_size", 0.1)
        self.declare_parameter("use_undistort", False)
        self.declare_parameter("use_left_camera", True)
        self.declare_parameter("marker_tags", "")

        self.marker_size = float(self.get_parameter("marker_size").value)
        self.use_undistort = self.get_parameter("use_undistort").value
        self.use_left_camera = self.get_parameter("use_left_camera").value

        raw_tags = self.get_parameter("marker_tags").value

        try:
            self.marker_tags = json.loads(raw_tags) if raw_tags else {}
        except Exception:
            self.marker_tags = {}

        self.get_logger().info(f"Loaded marker_tags: {self.marker_tags}")

        # -------------------------
        # CV
        # -------------------------
        self.bridge = CvBridge()
        self.camera_matrix = None
        self.dist_coeffs = None

        # -------------------------
        # SUBS
        # -------------------------
        self.create_subscription(
            CameraInfo,
            "/camera/head/front/camera_info",
            self.info_cb,
            qos_profile_sensor_data
        )

        self.create_subscription(
            CompressedImage,
            "/camera/head/front/image_raw/compressed",
            self.image_cb,
            qos_profile_sensor_data
        )

        # -------------------------
        # PUBS
        # -------------------------
        self.pub = self.create_publisher(MarkerArray, "/aruco/markers", 10)

        # -------------------------
        # ARUCO (NEW API)
        # -------------------------
        self.dictionary = cv2.aruco.getPredefinedDictionary(
            cv2.aruco.DICT_5X5_250
        )

        self.params = cv2.aruco.DetectorParameters()

        self.detector = cv2.aruco.ArucoDetector(
            self.dictionary,
            self.params
        )

        self.get_logger().info("Aruco detector READY (OpenCV modern API)")

    # -------------------------------------------------
    # CAMERA INFO
    # -------------------------------------------------
    def info_cb(self, msg):
        self.camera_matrix = np.array(msg.k).reshape(3, 3)
        self.dist_coeffs = np.array(msg.d)

    # -------------------------------------------------
    # IMAGE CALLBACK
    # -------------------------------------------------
    def image_cb(self, msg):

        if self.camera_matrix is None:
            return

        np_arr = np.frombuffer(msg.data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if frame is None:
            return

        h, w = frame.shape[:2]

        # stereo split
        if self.use_left_camera:
            frame = frame[:, :w // 2]
        else:
            frame = frame[:, w // 2:]

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # -------------------------
        # DETECTION
        # -------------------------
        corners, ids, rejected = self.detector.detectMarkers(gray)

        out = MarkerArray()
        out.header = msg.header

        if ids is None:
            self.pub.publish(out)
            return

        for i, marker_id in enumerate(ids.flatten()):

            c = corners[i][0].astype(np.float32)

            # ======================================================
            # POSE ESTIMATION (MODERNO: solvePnP)
            # ======================================================
            obj_points = np.array([
                [-self.marker_size/2,  self.marker_size/2, 0],
                [ self.marker_size/2,  self.marker_size/2, 0],
                [ self.marker_size/2, -self.marker_size/2, 0],
                [-self.marker_size/2, -self.marker_size/2, 0],
            ], dtype=np.float32)

            success, rvec, tvec = cv2.solvePnP(
                obj_points,
                c,
                self.camera_matrix,
                self.dist_coeffs
            )

            if not success:
                continue

            # -------------------------------------------------
            # NAME
            # -------------------------------------------------
            name = self.marker_tags.get(str(marker_id), "unknown")

            self.get_logger().info(
                f"Detected marker {marker_id}: {name}"
            )

            # -------------------------------------------------
            # ROS MESSAGE
            # -------------------------------------------------
            m = Marker()
            m.header = msg.header
            m.id = int(marker_id)

            m.pose.header = msg.header

            m.pose.pose.position.x = float(tvec[0])
            m.pose.pose.position.y = float(tvec[1])
            m.pose.pose.position.z = float(tvec[2])

            m.pose.pose.orientation.w = 1.0

            m.pixel_x = float(np.mean(c[:, 0]))
            m.pixel_y = float(np.mean(c[:, 1]))

            out.markers.append(m)

        self.pub.publish(out)


# -------------------------------------------------
# MAIN
# -------------------------------------------------
def main():
    rclpy.init()
    node = ArucoDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()