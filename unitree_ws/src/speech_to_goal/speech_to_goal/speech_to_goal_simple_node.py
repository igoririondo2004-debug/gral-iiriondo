import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from aruco_markers_msgs.msg import MarkerArray
from geometry_msgs.msg import PoseStamped

import re


class SpeechToGoal(Node):

    def __init__(self):
        super().__init__('speech_to_goal')

        # name -> (x,y)
        self.markers = {}

        # -----------------------------
        # SUBS
        # -----------------------------
        self.create_subscription(
            MarkerArray,
            '/aruco/markers_mapping',
            self.marker_cb,
            10
        )

        self.create_subscription(
            String,
            '/speech_text',
            self.speech_cb,
            10
        )

        # -----------------------------
        # GOAL PUB (ROS1 bridge compatible)
        # -----------------------------
        self.goal_pub = self.create_publisher(
            PoseStamped,
            '/move_base_simple/goal',
            10
        )

        self.get_logger().info("SpeechToGoal ready")

    # -----------------------------
    # UPDATE MAP
    # -----------------------------
    def marker_cb(self, msg):

        self.markers.clear()

        for m in msg.markers:

            # ⚠️ aquí asumimos que el mapper ya pone el nombre en text o id fallback
            name = str(m.id)

            self.markers[name.lower()] = (
                m.pose.pose.position.x,
                m.pose.pose.position.y
            )

    # -----------------------------
    # SPEECH PARSER
    # -----------------------------
    def speech_cb(self, msg):

        text = msg.data.lower().strip()
        self.get_logger().info(f"Speech: {text}")

        # -------------------------------------------------
        # 1. NORMALIZACIÓN DE FRASES
        # -------------------------------------------------
        text = text.replace("al la", "a la")  # fix common noise

        triggers = [
            "ve a la",
            "ve al",
            "muevete a la",
            "muevete al",
            "llévame a la",
            "llévame al",
            "ir a la",
            "ir al",
            "dirígete a la",
            "dirigete a la",
            "dirígete al",
            "dirigete al",
            "anda a la",
            "anda al"
        ]

        target = None

        # -------------------------------------------------
        # 2. DETECCIÓN SIMPLE DE INTENCIÓN
        # -------------------------------------------------
        for t in triggers:
            if t in text:
                target = text.split(t)[-1].strip()
                break

        if target is None:
            self.get_logger().warn("No navigation intent detected")
            return

        target = target.lower()

        # -------------------------------------------------
        # 3. MATCH CON MAPA
        # -------------------------------------------------
        if target not in self.markers:
            self.get_logger().warn(f"No marker found: {target}")
            return

        x, y = self.markers[target]

        self.get_logger().info(f"GO → {target}")

        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.header.stamp = self.get_clock().now().to_msg()

        goal.pose.position.x = float(x)
        goal.pose.position.y = float(y)
        goal.pose.orientation.w = 1.0

        self.goal_pub.publish(goal)

def main():
    rclpy.init()
    node = SpeechToGoal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()