import math


def xyz2lab_nonlinear_transform(t):
    if t > 0.008856:
        return math.pow(t, 1. / 3)
    else:
        return 7.787 * t + 16. / 116


def rgb2xyz_nonlinear_transform(t):
    if t <= 0.04045:
        return t / 12.92
    else:
        return math.pow(((t + 0.055) / 1.055), 2.4)
