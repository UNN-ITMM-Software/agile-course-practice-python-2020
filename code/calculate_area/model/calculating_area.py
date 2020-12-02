import math


class InvalidFigureError(Exception):
    pass


class Figure:
    def __init__(self, a=1, r=1, h=1, l=1):
        if isinstance(a, bool) or isinstance(r, bool) \
                or isinstance(h, bool) or isinstance(l, bool):
            raise InvalidFigureError('invalid data type')
        if isinstance(a, (int, float)) and isinstance(r, (int, float)) \
                and isinstance(h, (int, float)) and isinstance(l, (int, float)):
            if a <= 0 or r <= 0 or h <= 0 or l <= 0:
                raise InvalidFigureError('values cannot be less than 0')
        else:
            raise InvalidFigureError('invalid data type')
        self.a = a
        self.r = r
        self.h = h
        self.l = l

    def calculate_area_cone(self):
        return round(math.pi * self.r * (self.r + self.l), 3)

    def calculate_area_cube(self):
        return round(6 * self.a * self.a, 3)

    def calculate_area_cylinder(self):
        return round(2 * math.pi * self.r * (self.r + self.h), 3)

    def calculate_area_sphere(self):
        return round(4 * math.pi * self.r * self.r, 3)
