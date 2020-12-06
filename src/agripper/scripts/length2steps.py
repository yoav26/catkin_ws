import math
import numpy as np

STEPS_PER_REV = 400  # [S][steps/rev]
LEN_PER_REV = 30  # [D][mm/rev]
e = STEPS_PER_REV / LEN_PER_REV  # [e][steps/mm]
Cst3 = 400 / 80  # [steps/mm]


def length2steps(x, y, z):

    st1 = int(x * e)
    st2 = -int(y * e)
    st3 = -int(z * Cst3)
    steps = [st1, st2, st3]
    #  print(steps)
    return steps

