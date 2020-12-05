from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math
from geometric_func.WorkSpace import workspace
from geometric_func.DirectKinmatics import sensor_location
from geometric_func.InverseKinmatics import joints_angles


cordmat = workspace()
x = cordmat[:, 0]
y = cordmat[:, 1]
z = cordmat[:, 2]

angles = joints_angles(-25, 100, 25)
teta1 = angles[0]
teta2 = angles[1]
teta3 = angles[2]
links = sensor_location(teta1, teta2, teta3, 0, 0)
# print(links)

"""r = 9  # [mm]
t = np.linspace(0, 50, 100)
#ax.plot([links[4][0] + r*math.cos(t)], [links[4][1] + r*math.sin(t)], [links[4][2]])
circle_cord = r*math.cos(t) + 1"""


fig = plt.figure()
ax = plt.axes(projection='3d')

#ax.plot3D(cordmat[:, 0], cordmat[:, 1], cordmat[:, 2], '.')
# ax.plot(cordmat[:, 0], cordmat[:, 1], cordmat[:, 2], '.')
# ax.scatter(x, y, z, c='m', marker='.')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

ax.plot([-25, 25, 25, -25, -25], [100, 100, 100, 100, 100], [-25, -25, 25, 25, -25])

ax.plot([0, 0], [0, 0], [0, links[0][2]])
ax.plot([0, 0], [0, 0], [links[0][2], links[1][2]])
ax.plot([links[1][0], links[2][0]], [links[1][1], links[2][1]], [links[1][2], links[2][2]])
ax.plot([links[2][0], links[3][0]], [links[2][1], links[3][1]], [links[2][2], links[3][2]])
# ax.plot([links[3][0], links[4][0]], [links[3][1], links[4][1]], [links[3][2], links[4][2]])

plt.show()


# ax.scatter(xs, ys, zs, c='r', marker='o')