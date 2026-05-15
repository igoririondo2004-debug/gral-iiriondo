#!/usr/bin/env python3.8

import rclpy
from rclpy.node import Node
from std_msgs.msg import Empty
import time

import robot_interface as sdk


class StandingModeNode(Node):
    def __init__(self):
        super().__init__('standing_mode')

        self.declare_parameter('robot_ip', '192.168.123.161')
        self.robot_ip = self.get_parameter('robot_ip').value

        self.udp = sdk.UDP(0xee, 8080, self.robot_ip, 8082)
        self.cmd = sdk.HighCmd()
        self.state = sdk.HighState()
        self.udp.InitCmdData(self.cmd)

        self.cmd.mode = 0
        self.cmd.gaitType = 0
        self.cmd.speedLevel = 0
        self.cmd.footRaiseHeight = 0.0
        self.cmd.bodyHeight = 0.0
        self.cmd.euler = [0.0, 0.0, 0.0]
        self.cmd.velocity = [0.0, 0.0]
        self.cmd.yawSpeed = 0.0

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

        self.get_logger().info(f"StandingMode node running. Robot IP: {self.robot_ip}")

    def send_repeated_command(self, mode, duration=1.0):
        self.get_logger().info(f"Sending mode {mode} for {duration} sec")
        self.cmd.mode = mode

        start_time = time.time()
        while time.time() - start_time < duration:
            self.udp.SetSend(self.cmd)
            self.udp.Send()
            time.sleep(0.02)

    def stand_up_callback(self, msg):
        self.get_logger().info("Stand UP triggered")
        self.send_repeated_command(mode=6, duration=1.0)

    def stand_down_callback(self, msg):
        self.get_logger().info("Stand DOWN triggered")
        self.send_repeated_command(mode=5, duration=1.0)


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
