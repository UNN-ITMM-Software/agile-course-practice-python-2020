import math


def f(t):
    if t > 0.008856:
        return math.pow(t, 1. / 3)
    else:
        return 7.787 * t + 16. / 116
