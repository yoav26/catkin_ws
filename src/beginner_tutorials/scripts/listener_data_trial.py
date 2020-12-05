#!/usr/bin/env python

# simple tutorial node


import rospy
# from std_msgs.msg import AngleArray
from beginner_tutorials.msg import AngleArray


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' I heard ')
    print(data)


#def callback1(data):
    #rospy.loginfo(rospy.get_caller_id() + ' I heard from %i', data.data)


#def callback2(data):
    #rospy.loginfo(rospy.get_caller_id() + ' I heard %i', data.data)


def listener_data_trial():

    rospy.init_node('listener_data_trial', anonymous=True)

    rospy.Subscriber('angle/custom', AngleArray, callback)

#    rospy.Subscriber('alpha', Float32, callback1)
#    rospy.Subscriber('beta', Float32, callback2)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener_data_trial()
