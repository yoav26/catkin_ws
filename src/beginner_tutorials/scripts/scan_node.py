#!/usr/bin/env python
import math
import numpy as np
import rospy
from std_msgs.msg import Float32MultiArray, Float32
from DirectKinmatics import sensor_location
from InverseKinmatics import joints_angles

POS2RAD = (2 * math.pi) / 4096
RAD2POS = 4096 / (2 * math.pi)
ZERO_OFFSET = 4096/2
angles = np.array([0.0, 0.0, 0.0])
joints_angles_rad = [0.0, 0.0, 0.0]
angles_msg = Float32MultiArray()
location = Float32MultiArray()
l4 = 31.5
delta = 1

g = None
h = None

pub_location = rospy.Publisher("location", Float32MultiArray, queue_size=10)


def joints_angle_read(data):
    global POS2RAD
    global ZERO_OFFSET
    global joints_angles_rad

    rospy.loginfo(rospy.get_caller_id() + ' \n --Got the joints angles: %f %f %f', data.data[0], data.data[1], data.data[2])
    joints_angles_raw = data.data
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
   # global alpha
    global g
 #   rospy.loginfo('\n --Got the alpha: %i Degree', data.data)
    g = data.data * math.pi/180
   # print(' --alpha:         {} RAD'.format(alpha))


def beta(data):
    #global beta
    global h
    rospy.loginfo('\n --Got the beta: %i Degree', data.data)
    h = data.data * math.pi/180
    #print(' --beta:         {} RAD'.format(beta))


def scan_node():
    global angles
    global g
    global h
    rospy.init_node('scan_node', anonymous=True)
    pub1 = rospy.Publisher("write/angles", Float32MultiArray, queue_size=10)

    #rospy.Subscriber('read/angles_read', Float32MultiArray, joints_angle_read)
    rospy.Subscriber('read/alpha', Float32, alpha)
    rospy.Subscriber('read/beta', Float32, beta)

    # rospy.Subscriber('load', Float32MultiArray, beta) # for tourqe calc
    # Creates the scan matrix
    plain_offset = -l4
    x7 = (range(-25, 25, delta))
    y7 = (range(25, -25, -delta))
    z7 = plain_offset * np.ones(len(y7))
    for_dim = np.zeros(len(y7))
    for_dim[-1] = 1
    scan_matrix = np.array([x7, y7, z7, for_dim])
    #[a04, q5, q7] = sensor_location(joints_angles_rad[0], joints_angles_rad[1], joints_angles_rad[2], g, 0)
    # world_points = a04.dot(scan_matrix)
    print(g)
    # calc World's points
    i = 0
    angles_mat = list(np.ones(len(y7)))
    while i < len(y7):
        #some_angles = joints_angles(world_points[0, i], world_points[1, i], world_points[2, i])
        #angles_mat[i] = some_angles
        i += 1
    angles_mat = np.transpose(angles_mat)

    #rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        if g:
            [a04, q5, q7] = sensor_location(joints_angles_rad[0], joints_angles_rad[1], joints_angles_rad[2], g, 0)
            print(a04)
            print('\n')
            print(g)
            print(h)
            print('\n')
        #rate.sleep()
        rospy.spin()

'''def joints_angles(x, y, z):
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
'''

if __name__ == '__main__':
    try:
        scan_node()
    except rospy.ROSInterruptException:
        pass