import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from sensor_msgs.msg import CompressedImage, CameraInfo
from cv_bridge import CvBridge

import numpy as np
import cv2
import json
import os
import yaml
from ament_index_python.packages import get_package_share_directory

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

        self.marker_size = float(self.get_parameter("marker_size").value)
        self.use_undistort = self.get_parameter("use_undistort").value
        self.use_left_camera = self.get_parameter("use_left_camera").value

        # -------------------------
        # LOAD MARKER TAGS
        # -------------------------
        try:
            pkg_share = get_package_share_directory('aruco_detector')
            yaml_path = os.path.join(pkg_share, 'config', 'aruco_detector.yaml')

            with open(yaml_path, 'r') as f:
                config = yaml.safe_load(f)

            self.marker_tags = config['aruco_detector_node']['ros__parameters'].get('marker_tags', '{}')

            if isinstance(self.marker_tags, str):
                self.marker_tags = json.loads(self.marker_tags)

        except Exception as e:
            self.get_logger().warn(f"Failed to load marker_tags: {e}")
            self.marker_tags = {}

        self.get_logger().info(f"Loaded marker_tags: {self.marker_tags}")

        # -------------------------
        # CV & CAMERA
        # -------------------------
        self.bridge = CvBridge()
        self.camera_matrix = None
        self.dist_coeffs = None

        # -------------------------
        # SUBSCRIPTIONS
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
        # PUBLISHER
        # -------------------------
        self.pub = self.create_publisher(MarkerArray, "/aruco/markers", 10)

        # -------------------------
        # ARUCO SETUP (NEW API)
        # -------------------------
        self.dictionary = cv2.aruco.getPredefinedDictionary(
            cv2.aruco.DICT_5X5_250
        )

        self.params = cv2.aruco.DetectorParameters()

        # NEW OpenCV 4.7+ detector
        self.detector = cv2.aruco.ArucoDetector(
            self.dictionary,
            self.params
        )

        self.get_logger().info("Aruco detector READY")

    # -------------------------
    # CAMERA INFO
    # -------------------------
    def info_cb(self, msg):
        self.camera_matrix = np.array(msg.k).reshape(3, 3)
        self.dist_coeffs = np.array(msg.d)

    # -------------------------
    # IMAGE CALLBACK
    # -------------------------
    def image_cb(self, msg):

        if self.camera_matrix is None or self.dist_coeffs is None:
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
        # DETECTION (NEW API)
        # -------------------------
        corners, ids, rejected = self.detector.detectMarkers(gray)

        out = MarkerArray()
        out.header = msg.header

        if ids is None:
            self.pub.publish(out)
            return

        for i, marker_id in enumerate(ids.flatten()):

            c = corners[i][0].astype(np.float32)

            # -------------------------
            # POSE ESTIMATION
            # -------------------------
            obj_points = np.array([
                [-self.marker_size / 2,  self.marker_size / 2, 0],
                [ self.marker_size / 2,  self.marker_size / 2, 0],
                [ self.marker_size / 2, -self.marker_size / 2, 0],
                [-self.marker_size / 2, -self.marker_size / 2, 0],
            ], dtype=np.float32)

            success, rvec, tvec = cv2.solvePnP(
                obj_points,
                c,
                self.camera_matrix,
                self.dist_coeffs
            )

            if not success:
                continue

            # -------------------------
            # R -> quaternion
            # -------------------------
            R, _ = cv2.Rodrigues(rvec)
            trace = np.trace(R)

            if trace > 0:
                S = np.sqrt(trace + 1.0) * 2
                qw = 0.25 * S
                qx = (R[2, 1] - R[1, 2]) / S
                qy = (R[0, 2] - R[2, 0]) / S
                qz = (R[1, 0] - R[0, 1]) / S
            else:
                if (R[0, 0] > R[1, 1]) and (R[0, 0] > R[2, 2]):
                    S = np.sqrt(1.0 + R[0, 0] - R[1, 1] - R[2, 2]) * 2
                    qw = (R[2, 1] - R[1, 2]) / S
                    qx = 0.25 * S
                    qy = (R[0, 1] + R[1, 0]) / S
                    qz = (R[0, 2] + R[2, 0]) / S
                elif R[1, 1] > R[2, 2]:
                    S = np.sqrt(1.0 + R[1, 1] - R[0, 0] - R[2, 2]) * 2
                    qw = (R[0, 2] - R[2, 0]) / S
                    qx = (R[0, 1] + R[1, 0]) / S
                    qy = 0.25 * S
                    qz = (R[1, 2] + R[2, 1]) / S
                else:
                    S = np.sqrt(1.0 + R[2, 2] - R[0, 0] - R[1, 1]) * 2
                    qw = (R[1, 0] - R[0, 1]) / S
                    qx = (R[0, 2] + R[2, 0]) / S
                    qy = (R[1, 2] + R[2, 1]) / S
                    qz = 0.25 * S

            # -------------------------
            # NAME
            # -------------------------
            name = self.marker_tags.get(str(marker_id), "unknown")
            self.get_logger().info(f"Detected marker {marker_id}: {name}")

            # -------------------------
            # ROS MESSAGE
            # -------------------------
            m = Marker()
            m.header = msg.header
            m.id = int(marker_id)

            m.pose.header = msg.header
            m.pose.pose.position.x = float(tvec[0])
            m.pose.pose.position.y = float(tvec[1])
            m.pose.pose.position.z = float(tvec[2])

            m.pose.pose.orientation.x = float(qx)
            m.pose.pose.orientation.y = float(qy)
            m.pose.pose.orientation.z = float(qz)
            m.pose.pose.orientation.w = float(qw)

            m.pixel_x = float(np.mean(c[:, 0]))
            m.pixel_y = float(np.mean(c[:, 1]))

            out.markers.append(m)

        self.pub.publish(out)


# -------------------------
# MAIN
# -------------------------
def main():
    rclpy.init()
    node = ArucoDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()