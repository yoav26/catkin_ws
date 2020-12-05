#!/usr/bin/env python
import math
import numpy as np
import rospy
from std_msgs.msg import Float32MultiArray
# from beginner_tutorials.msg import AngleArray

RAD2POS = 4096 / (2 * math.pi)
ZERO_OFFSET = 4096/2
angles = np.array([0.0, 0.0, 0.0])
a = Float32MultiArray()

'''numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)[source]'''


def talker_custom():
    global a
    global angles

    rospy.init_node('talker_custom', anonymous=True)
    pub1 = rospy.Publisher("write/angles", Float32MultiArray, queue_size=10)
    rate = rospy.Rate(35)  # 10hz

    xs = np.array(range(-25, 27, 2))
    zs = np.array(range(155, 103, -2))
    y = -137
    i = 0
    j = 0

    while not rospy.is_shutdown():
        #c = input('user input:')
        #print(c)
        x = xs[i]
        z = zs[j]
        if not(z == zs[-1]):
            angles = joints_angles(x, y, z)
            angles_deg = angles * 180 / math.pi
            #print(angles)
            i += 1
            if xs[i] == -25 or xs[i] == 25:
                rospy.logwarn('for Z')
                xs = np.flipud(xs)
                j += 1
                i = 0

            if angles_deg[1] < -130.0 or angles_deg[1] > 130.0:
                rospy.logwarn("this is not mice")
            rospy.logwarn(angles)
            a.data = angles * RAD2POS + ZERO_OFFSET
            rospy.loginfo(a)
            pub1.publish(a)
            rate.sleep()
        else:
            a.data = [2048, 2048, 2048]
            rospy.loginfo(a)
            pub1.publish(a)
            rate.sleep()


def joints_angles(x, y, z):
    # the func gets point and return the angles of the joints
    #  angles = np.array([0.0, 0.0, 0.0])
    l0 = 40
    l1 = 44
    l2 = 108
    l3 = 60
    l4 = 31.5
    z2 = z - (l0 + l1)
    d = math.sqrt(z2 ** 2 + y ** 2 + x ** 2)

    # Need to a add cases for x = 0**
    # teta1 = math.atan(y / x)
    teta1 = math.atan2(y, x) + math.pi / 2
    teta3 = math.acos((d ** 2 - (l3 ** 2 + l2 ** 2)) / (2 * l2 * l3))
    teta2 = math.atan2(math.sqrt(y ** 2 + x ** 2), z2) - math.asin((l3 * math.sin(teta3)) / d)

    # angles = np.array(teta1, teta2, teta3)
#    teta1_deg = teta1 * 180 / math.pi
#    teta2_deg = teta2 * 180 / math.pi
#    teta3_deg = teta3 * 180 / math.pi
#    print(teta1_deg)
#    print(teta2_deg)
#    print(teta3_deg)

    angles = np.array([teta1, teta2, teta3])
    return angles
# joints_angles(-25, 40, -25)


if __name__ == '__main__':
    try:
        talker_custom()
    except rospy.ROSInterruptException:
        pass