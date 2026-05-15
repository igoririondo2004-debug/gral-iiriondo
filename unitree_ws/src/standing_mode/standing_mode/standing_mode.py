#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Empty
import subprocess
import os

class StandingModeNode(Node):

    def __init__(self):
        super().__init__('standing_mode')

        # Absolute path to your working script in the src folder
        self.bridge_script = os.path.expanduser(
            "~/gral-iiriondo-main/unitree_ws/src/standing_mode/script/unitree_stand.py"
        )

        # Use Python 3.8 installed via pyenv (must exist)
        self.python38 = os.path.expanduser(
            "~/.pyenv/versions/3.8.18/bin/python"
        )

        self.lock = False  # prevents spamming commands

        # Subscribers
        self.create_subscription(
            Empty,
            '/stand_up',
            self.stand_up_callback,
            10
        )

        self.create_subscription(
            Empty,
            '/stand_down',
            self.stand_down_callback,
            10
        )

        self.get_logger().info("StandingMode ROS node started")

    # -------------------------
    # COMMAND EXECUTOR
    # -------------------------
    def run_bridge(self, command: str):
        if self.lock:
            self.get_logger().warn("Command ignored (robot busy)")
            return

        self.lock = True

        cmd = [
            self.python38,
            self.bridge_script,
            command
        ]

        # Ensure Python 3.8 can find the Unitree SDK
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.expanduser(
            "~/gral-iiriondo-main/unitree_ws/src/unitree_legged_sdk/lib/python/arm64"
        )

        self.get_logger().info(
            f"Executing: {cmd} with PYTHONPATH={env['PYTHONPATH']}"
        )

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, env=env)

            if result.returncode != 0:
                self.get_logger().error(f"Bridge failed:\n{result.stderr}")
            else:
                self.get_logger().info(result.stdout)

        except Exception as e:
            self.get_logger().error(f"Exception: {e}")

        self.lock = False

    # -------------------------
    # CALLBACKS
    # -------------------------
    def stand_up_callback(self, msg):
        self.get_logger().info("Stand UP triggered")
        self.run_bridge("stand_up")

    def stand_down_callback(self, msg):
        self.get_logger().info("Stand DOWN triggered")
        self.run_bridge("stand_down")


# -------------------------
# MAIN
# -------------------------
def main(args=None):
    rclpy.init(args=args)
    node = StandingModeNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()