#!/usr/bin/env python
import numpy as np
import math
import rospy
from std_msgs.msg import Float32MultiArray, Float32

RAD2POS = 4096 / (2 * math.pi)
POS2RAD = (2 * math.pi) / 4096
ZERO_OFFSET = 4096/2
alpha = 0.0
beta = 0.0
joints_angles_rad = [0.0, 0.0, 0.0]
location = Float32MultiArray()

pub_location = rospy.Publisher("location", Float32MultiArray, queue_size=10)


def joints_angle_read(data):
    global POS2RAD
    global ZERO_OFFSET
    global joints_angles_rad

    rospy.loginfo(rospy.get_caller_id() + ' \n --Got the joints angles: %f %f %f', data.data[0], data.data[1], data.data[2])
    joints_angles_raw = list(data.data)
    print(joints_angles_raw)
    joints_angles_rad[0] = (joints_angles_raw[0] - ZERO_OFFSET) * POS2RAD
    joints_angles_rad[1] = (joints_angles_raw[1] - ZERO_OFFSET) * POS2RAD
    joints_angles_rad[2] = (joints_angles_raw[2] - ZERO_OFFSET) * POS2RAD
    print(joints_angles_rad)
    # data.data[0], data.data[1], data.data[2]

    location.data = sensor_location(joints_angles_rad[0], joints_angles_rad[1], joints_angles_rad[2], alpha, beta)
    rospy.loginfo('location: %f %f %f', location.data[0], location.data[1], location.data[2])
    pub_location.publish(location)
    # rospy.loginfo('is radians #################################? : %f %f', alpha, beta)


def alpha(data):
    global alpha
    rospy.loginfo('\n --Got the alpha: %i Degree', data.data)
    alpha = data.data * math.pi/180
    print(' --alpha:         {} RAD'.format(alpha))


def beta(data):
    global beta
    rospy.loginfo('\n --Got the beta: %i Degree', data.data)
    beta = data.data * math.pi/180
    print(' --beta:         {} RAD'.format(beta))


def robotic_arm_listener_talker():
    rospy.init_node('robotic_arm_listener_talker', anonymous=True)

    rospy.Subscriber('read/angles_read', Float32MultiArray, joints_angle_read)
    rospy.Subscriber('read/alpha', Float32, alpha)
    rospy.Subscriber('read/beta', Float32, beta)
    # rospy.Subscriber('load', Float32MultiArray, beta) # for tourqe calc

    rospy.spin()


def sensor_location(t1, t2, t3, a, b):
    l0 = 40
    l1 = 44
    l2 = 108
    l3 = 60
    l4 = 31.5

# Base rotation about z axis
    c1 = math.cos(t1)
    s1 = math.sin(t1)
    a01 = np.array(((c1, -s1, 0, 0), (s1, c1, 0, 0), (0, 0, 1, l0), (0, 0, 0, 1)))
    # print(a01)

# 2nd joint rotation about x axis
    c2 = math.cos(t2)
    s2 = math.sin(t2)
    a12 = np.array(((1, 0, 0, 0), (0, c2, -s2, 0), (0, s2, c2, l1), (0, 0, 0, 1)))
    # print(a12)

# 3rd joint rotation about x axis
    c3 = math.cos(t3)
    s3 = math.sin(t3)
    a23 = np.array(((1, 0, 0, 0), (0, c3, -s3, 0), (0, s3, c3, l2), (0, 0, 0, 1)))
    # print(a23)

# Displacement in Z3 coordinate system
    a34 = np.array(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, l3), (0, 0, 0, 1)))

    ca = math.cos(a)
    sa = math.sin(a)
    ax = np.array(((1, 0, 0, 0), (0, ca, -sa, 0), (0, sa, ca, 0), (0, 0, 0, 1)))

    cb = math.cos(b)
    sb = math.sin(b)
    ay = np.array(((cb, 0, sb, 0), (0, 1, 0, 0), (-sb, 0, cb, 0), (0, 0, 0, 1)))
    am = np.array(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, l4), (0, 0, 0, 1)))
    a04 = a01.dot(a12.dot(a23.dot(a34.dot(ax.dot(ay.dot(am))))))
    # print(a04)
    p0 = a04.dot([0, 0, 0, 1])
    # print(p0)
    q3 = a01.dot(a12.dot(a23.dot([0, 0, 0, 1])))
    q4 = a01.dot(a12.dot(a23.dot(a34.dot([0, 0, 0, 1]))))
    # q5 = a01.dot(a12.dot(a23.dot(a34.dot([0, 0, l4, 1]))))
    q5 = a01.dot(a12.dot(a23.dot(a34.dot(ax.dot(ay.dot(am.dot([0, 0, 0, 1])))))))
    # origin = [0, 0, 0]
    first_link = [0, 0, l0]
    second_link = [0, 0, l1+l0]
    third_link = [q3[0], q3[1], q3[2]]
    forth_link = [q4[0], q4[1], q4[2]]
    fifth_link = [q5[0], q5[1], q5[2]]
    # print(q4)
    return q5


if __name__ == '__main__':
    robotic_arm_listener_talker()


'''if __name__ == '__main__':
    try:
        robotic_arm_listener_talker()
    except rospy.ROSInterruptException:
        pass'''

