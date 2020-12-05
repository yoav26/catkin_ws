import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri



def workspace():

    l0 = 40
    l1 = 44
    l2 = 105
    l3 = 60
    l4 = 31.5

    n = 10
    teta1 = 0   #-(2 * math.pi) / n
    teta2 = -5*math.pi/6
    teta3 = -5*math.pi/6
    alpha = -30*math.pi/180
    beta = -30*math.pi/180

    index = 0
    cordmat = np.zeros([n**5, 3])
    inermidval = np.zeros([3])

    for i in range(0, n):
        teta1 = teta1 + (2 * math.pi) / n
        for a in range(0, n):
            teta2 = teta2 + ((5/3) * math.pi) / n
            for b in range(0, n):
                teta3 = teta3 + ((5/3) * math.pi) / n
                """for c in range(0, n):
                    alpha = alpha + ((1/3) * math.pi) / n
                    for d in range(0, n):
                        beta = beta + ((1/3) * math.pi) / n"""
                inermidval[0] = (math.sin(teta1)) * (l2 * math.sin(teta2) + l3 * math.sin(teta2 + teta3))
                inermidval[1] = -((math.cos(teta1)) * (l2 * math.sin(teta2) + l3 * math.sin(teta2 + teta3)))
                inermidval[2] = l0 + l1 + l2 * math.cos(teta2) + l3 * math.cos(teta2 + teta3)

                cordmat[index, 0] = inermidval[0]
                cordmat[index, 1] = inermidval[1]
                cordmat[index, 2] = inermidval[2]
                index += 1
# print(cordmat)

    """fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(cordmat[:, 0], cordmat[:, 1], cordmat[:, 2], '.')
    #ax.plot(cordmat[:, 0], cordmat[:, 1], cordmat[:, 2], '.')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')"""

    return cordmat


# workspace()
