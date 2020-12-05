#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import String

steps = [0, 0, 0]
string_msg = String()

''' this func. goes home '''


def home():
    global steps

    rospy.init_node('home', anonymous=True)
    home_pub = rospy.Publisher("home", String, queue_size=10)
    string_msg.data = "go home"
    time.sleep(0.5)
    # rate = rospy.Rate(35)  # 10hz
    home_pub.publish(string_msg)
    rospy.loginfo(string_msg)


if __name__ == '__main__':
    try:
        home()
    except rospy.ROSInterruptException:
        pass
