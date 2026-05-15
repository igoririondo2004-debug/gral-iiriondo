#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def main():
    rospy.init_node("robot_description_topic_publisher", anonymous=False)
    publisher = rospy.Publisher("/robot_description", String, queue_size=1, latch=True)
    rate = rospy.Rate(1.0)

    while not rospy.is_shutdown():
        if rospy.has_param("/robot_description"):
            publisher.publish(rospy.get_param("/robot_description"))
            rospy.loginfo("Published /robot_description as a latched topic")
            rospy.spin()
            return
        rate.sleep()


if __name__ == "__main__":
    main()
