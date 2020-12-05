#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32

def talker():
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    pubn = rospy.Publisher('num', Int32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    num = 1
    rate = rospy.Rate(20) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()

       # rospy.loginfo(hello_str)
       # pub.publish(hello_str)
        rospy.loginfo(num)
        pubn.publish(num)
        num += 1
        rate.sleep()
        # rospy.spin()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
