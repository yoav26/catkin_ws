#!/usr/bin/env python

import math
import numpy as np
import rospy
from beginner_tutorials.msg import AngleArray

RAD2POS = 4096 / (2 * math.pi)
ZERO_OFFSET = 4096/2
a = 0
angles = np.array([0.0, 0.0, 0.0])


def talker_custom():
    global a
    global angles

    rospy.init_node('talker_custom', anonymous=True)
    pub1 = rospy.Publisher('angle/custom', AngleArray, queue_size=10)
    rate = rospy.Rate(5)  # 10hz
    a = AngleArray()

    a.alpha = 4
    a.beta = 5

    xs = np.array(range(-25, 27, 2))
    zs = np.array(range(30, 82, 2))
    y = -30
    i = 0
    j = 0

    while not rospy.is_shutdown():
        x = xs[i]
        z = zs[j]
        if not(z == 80):
            angles = joints_angles(x, y, z)
            angles_deg = angles * 180 / math.pi
            print(angles)

            a.theta1 = (angles[0] * RAD2POS) + ZERO_OFFSET  # <TODO> need to convert to clicks and add offset !!
            a.theta2 = (angles[1] * RAD2POS) + ZERO_OFFSET
            a.theta3 = (angles[2] * RAD2POS) + ZERO_OFFSET

            i += 1

            if xs[i] == -25 or xs[i] == 25:
                rospy.logwarn('for Z')
                xs = np.flipud(xs)
                j += 1
                i = 0

            if angles_deg[1] < -130.0 or angles_deg[1] > 130.0:
                rospy.logwarn("this is not mice")

            pub1.publish(a)
            rospy.loginfo(a)
            a.theta1 = 0.0
            a.theta2 = 0.0
            a.theta3 = 0.0
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