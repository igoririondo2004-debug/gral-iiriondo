import rclpy
from rclpy.node import Node

from aruco_markers_msgs.msg import MarkerArray, Marker
from visualization_msgs.msg import Marker as VizMarker
from visualization_msgs.msg import MarkerArray as VizArray
from nav_msgs.msg import Odometry
from std_msgs.msg import String

from ament_index_python.packages import get_package_share_directory

from object_recognition_interfaces.srv import AddObject

import os
import yaml
import json


class ArucoMapper(Node):

    def __init__(self):
        super().__init__('aruco_mapper')

        # -------------------------------------------------
        # LOAD NAMES
        # -------------------------------------------------
        yaml_path = os.path.join(
            get_package_share_directory("aruco_detector"),
            "config",
            "aruco_detector.yaml"
        )

        self.names = {}

        try:
            with open(yaml_path, "r") as f:
                data = yaml.safe_load(f)

            tags_json = data["aruco_detector_node"]["ros__parameters"]["marker_tags"]

            self.names = {
                int(k): str(v)
                for k, v in json.loads(tags_json).items()
            }

            self.get_logger().info(f"Loaded names: {self.names}")

        except Exception as e:
            self.get_logger().error(f"Failed loading YAML: {e}")

        # -------------------------------------------------
        # PATH
        # -------------------------------------------------
        ws_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "..")
        )

        self.source_config_path = os.path.join(
            ws_root,
            "src",
            "aruco_detector",
            "config"
        )

        os.makedirs(self.source_config_path, exist_ok=True)

        # -------------------------------------------------
        # STATE
        # -------------------------------------------------
        self.robot_xy = None
        self.map = {}

        # -------------------------------------------------
        # SUBS
        # -------------------------------------------------
        self.create_subscription(Odometry, '/odom', self.odom_cb, 10)
        self.create_subscription(MarkerArray, '/aruco/markers', self.marker_cb, 10)
        self.create_subscription(String, '/aruco/save_map', self.save_map_cb, 10)
        self.create_subscription(String, '/aruco/load_map', self.load_map_cb, 10)

        # -------------------------------------------------
        # PUBS
        # -------------------------------------------------
        self.pub_map = self.create_publisher(MarkerArray, '/aruco/markers_mapping', 10)
        self.pub_viz = self.create_publisher(VizArray, '/aruco/markers_viz', 10)

        # -------------------------------------------------
        # SERVICE: ADD MARKER
        # -------------------------------------------------
        self.add_srv = self.create_service(
            AddObject,
            '/aruco/add_marker',
            self.add_marker_cb
        )

        self.get_logger().info("Aruco Mapper Ready (+ /aruco/add_marker service)")

        # -------------------------------------------------
        self.timer = self.create_timer(0.2, self.publish)

    # -------------------------------------------------
    def odom_cb(self, msg):
        self.robot_xy = (
            msg.pose.pose.position.x,
            msg.pose.pose.position.y
        )

    # -------------------------------------------------
    def marker_cb(self, msg):

        if self.robot_xy is None:
            return

        rx, ry = self.robot_xy

        for m in msg.markers:

            name = self.names.get(m.id, str(m.id))

            if m.id in self.map:
                self.map[m.id]["x"] = float(rx)
                self.map[m.id]["y"] = float(ry)
                self.map[m.id]["z"] = 0.0
                self.map[m.id]["name"] = name
            else:
                self.map[m.id] = {
                    "x": float(rx),
                    "y": float(ry),
                    "z": 0.0,
                    "name": name
                }

    # -------------------------------------------------
    # SERVICE CALLBACK
    # -------------------------------------------------
    def add_marker_cb(self, request, response):

        # si ya existe EXACTAMENTE igual (nombre con espacios cuenta)
        for m in self.map.values():
            if m["name"] == request.name:
                response.success = False
                response.message = "Marker already exists with same name"
                return response

        # añadir nuevo marker manual
        new_id = max(self.map.keys(), default=-1) + 1

        self.map[new_id] = {
            "x": float(request.x),
            "y": float(request.y),
            "z": float(request.z),
            "name": request.name
        }

        response.success = True
        response.message = f"Marker added with id {new_id}"

        self.get_logger().info(f"Added manual marker: {request.name}")

        return response

    # -------------------------------------------------
    def publish(self):

        map_msg = MarkerArray()
        viz_msg = VizArray()

        now = self.get_clock().now().to_msg()

        for m_id, m in self.map.items():

            x, y, z = m["x"], m["y"], m["z"]

            # MAP
            frozen = Marker()
            frozen.id = m_id
            frozen.header.frame_id = "map"
            frozen.header.stamp = now

            frozen.pose.pose.position.x = x
            frozen.pose.pose.position.y = y
            frozen.pose.pose.position.z = z

            map_msg.markers.append(frozen)

            # SPHERE
            sphere = VizMarker()
            sphere.header.frame_id = "map"
            sphere.header.stamp = now
            sphere.ns = "aruco_spheres"
            sphere.id = m_id
            sphere.type = VizMarker.SPHERE
            sphere.action = VizMarker.ADD

            sphere.pose.position.x = x
            sphere.pose.position.y = y
            sphere.pose.position.z = z

            sphere.scale.x = 0.15
            sphere.scale.y = 0.15
            sphere.scale.z = 0.15

            sphere.color.a = 1.0
            sphere.color.g = 1.0

            viz_msg.markers.append(sphere)

            # TEXT
            text = VizMarker()
            text.header.frame_id = "map"
            text.header.stamp = now
            text.ns = "aruco_text"
            text.id = m_id + 10000
            text.type = VizMarker.TEXT_VIEW_FACING
            text.action = VizMarker.ADD

            text.pose.position.x = x
            text.pose.position.y = y
            text.pose.position.z = z + 0.35

            text.scale.z = 0.25

            text.color.a = 1.0
            text.color.r = 1.0
            text.color.g = 1.0
            text.color.b = 1.0

            text.text = m["name"]

            viz_msg.markers.append(text)

        self.pub_map.publish(map_msg)
        self.pub_viz.publish(viz_msg)

    # -------------------------------------------------
    def save_map_cb(self, msg):

        filename = msg.data.strip()
        if not filename:
            return

        path = os.path.join(self.source_config_path, filename + ".yaml")

        data = {"markers": {}}

        for m_id, m in self.map.items():
            data["markers"][str(m_id)] = {
                "x": m["x"],
                "y": m["y"],
                "z": m["z"],
                "name": m["name"]
            }

        with open(path, "w") as f:
            yaml.dump(data, f, sort_keys=True)

        self.get_logger().info(f"Saved map -> {path}")

    # -------------------------------------------------
    def load_map_cb(self, msg):

        filename = msg.data.strip()
        if not filename:
            return

        path = os.path.join(self.source_config_path, filename + ".yaml")

        if not os.path.exists(path):
            self.get_logger().error(f"Missing file: {path}")
            return

        with open(path, "r") as f:
            data = yaml.safe_load(f) or {}

        for k, v in data.get("markers", {}).items():

            m_id = int(k)

            if m_id in self.map:
                continue

            self.map[m_id] = {
                "x": float(v["x"]),
                "y": float(v["y"]),
                "z": float(v.get("z", 0.0)),
                "name": v.get("name", self.names.get(m_id, str(m_id)))
            }


def main():
    rclpy.init()
    node = ArucoMapper()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()