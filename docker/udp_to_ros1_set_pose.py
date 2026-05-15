#!/usr/bin/env python3
import json
import socket

import rospy
from geometry_msgs.msg import Pose


UDP_HOST = "127.0.0.1"
UDP_PORT = 15301


def main():
    rospy.init_node("udp_to_set_pose_bridge", anonymous=False)
    pub = rospy.Publisher("/slamware_ros_sdk_server_node/set_pose", Pose, queue_size=1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_HOST, UDP_PORT))
    sock.settimeout(1.0)

    rospy.loginfo("Forwarding local UDP relay to ROS1 /slamware_ros_sdk_server_node/set_pose")

    while not rospy.is_shutdown():
        try:
            data, _addr = sock.recvfrom(65535)
        except socket.timeout:
            continue

        payload = json.loads(data.decode("utf-8"))
        msg = Pose()
        msg.position.x = payload["position"]["x"]
        msg.position.y = payload["position"]["y"]
        msg.position.z = payload["position"]["z"]
        msg.orientation.x = payload["orientation"]["x"]
        msg.orientation.y = payload["orientation"]["y"]
        msg.orientation.z = payload["orientation"]["z"]
        msg.orientation.w = payload["orientation"]["w"]
        pub.publish(msg)
        rospy.loginfo("Published /slamware_ros_sdk_server_node/set_pose from UDP relay")


if __name__ == "__main__":
    main()
