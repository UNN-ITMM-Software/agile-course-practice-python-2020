import math


def calculate_volume_cube(r=1):
    if r < 0:
        raise ValueError("values must be greater than 0")
    return r ** 3


def calculate_volume_sphere(r=1):
    if r < 0:
        raise ValueError("values must be greater than 0")
    return round(4 / 3 * math.pi * r ** 3, 3)


def calculate_volume_cylinder(r=1, h=1):
    if r < 0 or h < 0:
        raise ValueError("values must be greater than 0")
    return round(math.pi * r ** 2 * h, 3)
