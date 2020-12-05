#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

#flag = Int32()


def tourqe_enable():

    rospy.init_node('tourqe_enable', anonymous=True)
    tourqe_enable = rospy.Publisher("tourqe_enable", Int32, queue_size=10)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        flag = input('1 or 0 ?:')

        rospy.loginfo(flag)
        tourqe_enable.publish(flag)
        rate.sleep()


    #rospy.spin()


if __name__ == '__main__':
    try:
        tourqe_enable()
    except rospy.ROSInterruptException:
        pass
