import math

import numpy


class TriangleError(Exception):
    pass


class Triangle(object):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def get_ab(self):
        return math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)

    def get_bc(self):
        return math.sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2)

    def get_ca(self):
        return math.sqrt((self.x3 - +self.x1) ** 2 + (self.y3 - self.y1) ** 2)

    def is_triangle(self):
        if (self.x2 - self.x1) * (self.y3 - self.y1) == (self.x3 - self.x1) * (self.y2 - self.y1):
            return False
        return True

    def get_area(self): # площадь
        if not self.is_triangle():
            raise TriangleError('This triangle is invalid! Check it!')
        return 0.5 * abs((self.x2 - self.x1) * (self.y3 - self.y1) -
                         (self.x3 - self.x1) * (self.y2 - self.y1))

    def get_perimeter(self):  # периметр
        if not self.is_triangle():
            raise TriangleError('This triangle is invalid! Check it!')
        return self.get_ab() + self.get_bc() + self.get_ca()

    def get_circumcircle_radius(self): # описанная окружность
        if not self.is_triangle():
            raise TriangleError('This triangle is invalid! Check it!')
        return self.get_ab() * self.get_bc() * self.get_ca() / (4 * Triangle.get_area(self))

    def get_circumcircle_center(self):
        if not self.is_triangle():
            raise TriangleError('This triangle is invalid! Check it!')
        k1 = ((self.x2 ** 2 + self.y2 ** 2) - (self.x3 ** 2 + self.y3 ** 2)) / (
                2 * ((self.x2 - self.x3) * (self.y1 - self.y2) - (self.x1 - self.x2) * (self.y2 - self.y3)))
        k2 = ((self.x1 ** 2 + self.y1 ** 2) - (self.x2 ** 2 + self.y2 ** 2)) / (
                2 * ((self.x2 - self.x3) * (self.y1 - self.y2) - (self.x1 - self.x2) * (self.y2 - self.y3)))
        return [k1 * (self.y1 - self.y2) - k2 * (self.y2 - self.y3),
                -k1 * (self.x1 - self.x2) + k2 * (self.x2 - self.x3)]

    def get_incircle_radius(self):  # вписанная окружность
        if not self.is_triangle():
            raise TriangleError('This triangle is invalid! Check it!')
        return 2 * Triangle.get_area(self) / Triangle.get_perimeter(self)

    def get_incircle_center(self):
        if not self.is_triangle():
            raise TriangleError('This triangle is invalid! Check it!')
        a1 = (self.get_ca() * (self.y2 - self.y1) + self.get_ab() * (self.y3 - self.y1)) / (
                self.get_ca() * (self.x2 - self.x1) + self.get_ab() * (self.x3 - self.x1))
        a2 = (self.get_bc() * (self.y1 - self.y2) + self.get_ab() * (self.y3 - self.y2)) / (
                self.get_bc() * (self.x1 - self.x2) + self.get_ab() * (self.x3 - self.x2))
        m1 = numpy.array([[a1, -1.0],
                          [a2, -1.0]])
        v1 = numpy.array(
            [-self.y1 + self.x1 * a1,
             -self.y2 + self.x2 * a2])
        return list(numpy.linalg.solve(m1, v1))

    def get_triangle_type_by_sides(self):
        if not self.is_triangle():
            raise TriangleError('This triangle is invalid! Check it!')
        if (abs(self.get_ab() - self.get_bc()) < 1e-10 and abs(self.get_ab() - self.get_ca()) > 1e-10) or (
                abs(self.get_bc() - self.get_ca()) < 1e-10 and
                abs(self.get_ab() - self.get_ca()) > 1e-10) or (
                abs(self.get_ab() - self.get_ca()) < 1e-10 and
                abs(self.get_ab() - self.get_bc()) > 1e-10):
            return "isosceles"  # равнобедренный
        elif abs(self.get_ab() - self.get_bc()) < 1e-10 and abs(self.get_bc() - self.get_ca()) < 1e-10:
            return "equilateral"  # равносторонний
        return "various"  # разносторонний

    def get_triangle_type_by_angles(self):
        if not self.is_triangle():
            raise TriangleError('This triangle is invalid! Check it!')
        if (self.get_ab() ** 2 + self.get_bc() ** 2 == self.get_ca() ** 2) or (
                self.get_ab() ** 2 + self.get_ca() ** 2 == self.get_bc() ** 2) or (
                self.get_ca() ** 2 + self.get_bc() ** 2 == self.get_ab() ** 2):
            return "right"  # прямоугольный
        elif (self.get_ab() ** 2 + self.get_bc() ** 2 > self.get_ca() ** 2) and (
                self.get_ab() ** 2 + self.get_ca() ** 2 > self.get_bc() ** 2) and (
                self.get_ca() ** 2 + self.get_bc() ** 2 > self.get_ab() ** 2):
            return "acute"  # остроугольный
        return "obtuse"  # тупоугольный
