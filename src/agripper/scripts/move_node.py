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


def move_node():
    global steps

    rospy.init_node('move_node', anonymous=True)
    steps_pub = rospy.Publisher("write/steps", Float32MultiArray, queue_size=10)
    # rate = rospy.Rate(35)  # 10hz

    while not rospy.is_shutdown():
        [x, y, z] = input('Insert location [x,y,z]: ')
        # x = input('Insert location [x,y,z]: ')
        if x > 550 or x < 0:
            rospy.logwarn('Out of range, insert value [0, 600]')
        else:
            steps = length2steps(x, y, z)
            rospy.loginfo(steps)
            steps_msg.data = steps
            steps_pub.publish(steps_msg)
    rospy.spin()


if __name__ == '__main__':
    try:
        move_node()
    except rospy.ROSInterruptException:
        pass
