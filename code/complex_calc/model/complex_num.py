import math


class ComplexNum:
    def __init__(self, re=0.0, im=0.0):
        self.re = re
        self.im = im

    def __str__(self):
        return '{}{}i'.format(self.re, (' + ' if self.im >= 0 else ' - ') + str(abs(self.im)))

    def __mul__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.re*other.re - self.im*other.im, self.re*other.im + self.im*other.re)
        elif isinstance(other, float) or isinstance(other, int):
            return ComplexNum(self.re * other, self.im * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.re + other.re, self.im + other.im)
        elif isinstance(other, float) or isinstance(other, int):
            return ComplexNum(self.re + other, self.im)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, ComplexNum):
            return self.__add__(-other)
        elif isinstance(other, float) or isinstance(other, int):
            return ComplexNum(self.re - other, self.im)

    def __rsub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return ComplexNum(other - self.re, -self.im)

    def __truediv__(self, other):
        if isinstance(other, ComplexNum):
            return self*other.conjugate() / (abs(other)**2)
        elif isinstance(other, float) or isinstance(other, int):
            return ComplexNum(self.re / other, self.im / other)

    def __eq__(self, other):
        if isinstance(other, ComplexNum):
            return self.re == other.re and self.im == other.im
        elif isinstance(other, float) or isinstance(other, int):
            return self.re == other

    def __ne__(self, other):
        if isinstance(other, ComplexNum):
            return self.re != other.re or self.im != other.im
        elif isinstance(other, float) or isinstance(other, int):
            return self.re != other

    def __rtruediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return other * self.conjugate() / (self.__abs__()**2)

    def __neg__(self):
        return ComplexNum(-self.re, -self.im)

    def conjugate(self):
        return ComplexNum(self.re, -self.im)

    def __abs__(self):
        return math.sqrt(self.re ** 2 + self.im ** 2)

    def eq_with_precision(self, other, precision=1e-10):
        return (other.re - precision < self.re < other.re + precision) and \
               (other.im - precision < self.im < other.im + precision)
