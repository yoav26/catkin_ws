#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
location = [0, 0, 0]


def callback(data):
    global location
    location = list(data.data)
    rospy.loginfo(rospy.get_caller_id() + 'I heard %f', data.data[0])
    print(data.data[0], data.data[1], data.data[2])


def location_listener():

    rospy.init_node('location_listener', anonymous=True)

    rospy.Subscriber('location', Float32MultiArray, callback)

    rospy.spin()


if __name__ == '__main__':
    location_listener()
