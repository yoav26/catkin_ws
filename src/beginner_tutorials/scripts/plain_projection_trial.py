import numpy as np
import math
from DirectKinmatics import sensor_location
from InverseKinmatics import joints_angles

DEG2RAD = math.pi / 180
l4 = 31.5

angles = np.array([60, 60, 90, 0, 0]) * DEG2RAD  # Insert in degree
[a04, q4, q5] = sensor_location(angles[0], angles[1], angles[2], angles[3], angles[4])
print(np.linalg.norm(q5-q4))



plain_offset = -l4
x7 = np.array(range(-20, 22, 2))
y7 = np.array(range(-20, 22, 2))
z71 = plain_offset * np.ones(len(y7))
z72 = (plain_offset-2) * np.ones(len(y7))

 # z7 = plain_offset * np.ones(len(y7))

size = len(y7) ** 2
scan_matrix = list(np.array([np.ones(size), np.ones(size), np.ones(size), np.ones(size)]))

i = 0
j = 0
index = 0

while index < size:

    scan_matrix[0][index] = x7[i]
    scan_matrix[1][index] = y7[j]
    if index < int(size/2):
        scan_matrix[2][index] = z71[i]
    elif index >= int(size/2):
        scan_matrix[2][index] = z72[i]
    i += 1
    index += 1

    if x7[i] == -20 or x7[i] == 20:
        scan_matrix[0][index] = x7[i]
        scan_matrix[1][index] = y7[j]
        if index < int(size / 2):
            scan_matrix[2][index] = z71[i]
        elif index >= int(size / 2):
            scan_matrix[2][index] = z72[i]
        x7 = np.flipud(x7)
        j += 1
        index += 1
        i = 0  # ??????

world_point_mat = a04.dot(scan_matrix)
#print(world_point_mat)

# calc World's points
h = 0
world_angles = (np.array([np.zeros(size), np.zeros(size), np.zeros(size)]))
while h < len(world_point_mat[0]):
    some_angles = joints_angles(world_point_mat[0][h], world_point_mat[1][h], world_point_mat[2][h])
    world_angles[0][h] = some_angles[0]
    world_angles[1][h] = some_angles[1]
    world_angles[2][h] = some_angles[2]
    h += 1

# world_anglesT = np.transpose(world_angles)
