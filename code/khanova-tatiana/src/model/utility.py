import math


def xyz2lab_nonlinear_transform(t):
    if t > 0.008856:
        return math.pow(t, 1. / 3)
    else:
        return 7.787 * t + 16. / 116


def xyz2lab_nonlinear_transform_inv(t):
    t3 = math.pow(t, 3)
    if t3 > 0.008856:
        return t3
    else:
        return (t - (16.0 / 116.0)) / 7.787


def rgb2xyz_nonlinear_transform(t):
    if t <= 0.04045:
        return t / 12.92
    else:
        return math.pow(((t + 0.055) / 1.055), 2.4)


def rgb2xyz_nonlinear_transform_inv(t):
    if t > 0.0031308:
        return (1.055 * math.pow(t, 1.0 / 2.4)) - 0.055
    else:
        return t * 12.92
