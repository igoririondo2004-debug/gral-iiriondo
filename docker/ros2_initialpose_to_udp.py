#!/usr/bin/env python3
import json
import socket
import sys

import rclpy
from geometry_msgs.msg import PoseWithCovarianceStamped
from rclpy.node import Node


UDP_HOST = "127.0.0.1"
UDP_PORT = 15301


class InitialPoseUdpForwarder(Node):
    def __init__(self):
        super().__init__("initialpose_to_udp_bridge")
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.create_subscription(PoseWithCovarianceStamped, "/initialpose", self._forward_pose, 10)
        self.get_logger().info("Forwarding ROS2 /initialpose to local UDP relay")

    def _forward_pose(self, msg):
        payload = {
            "position": {
                "x": msg.pose.pose.position.x,
                "y": msg.pose.pose.position.y,
                "z": msg.pose.pose.position.z,
            },
            "orientation": {
                "x": msg.pose.pose.orientation.x,
                "y": msg.pose.pose.orientation.y,
                "z": msg.pose.pose.orientation.z,
                "w": msg.pose.pose.orientation.w,
            },
        }
        self._sock.sendto(json.dumps(payload).encode("utf-8"), (UDP_HOST, UDP_PORT))
        self.get_logger().info(
            f"Forwarded /initialpose to UDP relay: x={payload['position']['x']:.3f}, y={payload['position']['y']:.3f}"
        )


def main():
    rclpy.init(args=sys.argv)
    node = InitialPoseUdpForwarder()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
