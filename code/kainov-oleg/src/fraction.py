import rational_math


class InvalidFractionError(Exception):
    pass


class Fraction:
    # The class represents rational number p/q, q!=0,
    # and the fraction is irreducible
    p = 0
    q = 1

    def __init__(self, p=0, q=1):
        if q == 0:
            raise InvalidFractionError('q cannot be equal to zero')
        common_divisor = rational_math.GCD(p, q)
        self.p = p / common_divisor
        self.q = q / common_divisor

    def __str__(self):
        return '{p}/{q}'.format(p=self.p, q=self.q)

    def __mul__(self, other):
        return Fraction(self.p * other.p, self.q * other.q)

    def __add__(self, other):
        common_multiple = rational_math.LCM(self.q, other.q)
        self_multiplier = common_multiple / self.q
        other_multiplier = common_multiple / other.q
        return Fraction(self.p * self_multiplier +
                        other.p * other_multiplier, common_multiple)

    def to_decimal(self):
        return self.p / float(self.q)

    def get_int_part(self):
        return self.p / self.q

    @staticmethod
    def from_decimal(decimal_number):
        int_part = int(decimal_number)
        frac_part = decimal_number - int_part
        frac_length = len(str(frac_part)) - 2  # Leading 0.

        q = pow(10, frac_length)
        p = int(frac_part * q) + int_part * q

        return Fraction(p, q)
