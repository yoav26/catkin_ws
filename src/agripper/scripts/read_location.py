#!/usr/bin/env python

import math
import numpy as np
import rospy
from std_msgs.msg import Float32MultiArray, Int32MultiArray
from length2steps import length2steps

steps = [0, 0, 0]
steps_msg = Float32MultiArray()

''' this func. takes INPUT: desired location 
            and give OUTPUT: number of steps '''


def cb_steps(data):
    current_steps = data.data
    rospy.loginfo("current_steps: %d %d %d", current_steps[0], current_steps[1],current_steps[2])


def read_location():
    global steps

    rospy.init_node('read_location', anonymous=True)
    rospy.Subscriber('read/current_step', Int32MultiArray, cb_steps)
    # rate = rospy.Rate(35)  # 10hz
    rospy.spin()


if __name__ == '__main__':
    try:
        read_location()
    except rospy.ROSInterruptException:
        pass
