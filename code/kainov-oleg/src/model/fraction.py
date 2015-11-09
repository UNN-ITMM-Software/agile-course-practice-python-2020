import re

from model import rational_math


class InvalidFractionError(Exception):
    pass


class Fraction:
    # The class represents rational number p/q, q!=0,
    # and the fraction is irreducible
    p = 0
    q = 1

    FRACTION_REGEXP = '^([-]?\d+)(?:[/](\d+))?$'

    @staticmethod
    def from_decimal(decimal_number):
        decimal_number = float(decimal_number)
        int_part = int(decimal_number)
        frac_part = decimal_number - int_part
        str_frac_part = str(frac_part)
        n_digits_after_point = len(str_frac_part) - \
            str_frac_part.index('.') - 1

        q = pow(10, n_digits_after_point)
        p = int(round(frac_part * q)) + int_part * q

        return Fraction(p, q)

    def __init__(self, p=0, q=1):
        if q == 0:
            raise InvalidFractionError('q cannot be equal to zero')
        common_divisor = rational_math.gcd(p, q)
        self.p = p / common_divisor
        self.q = q / common_divisor

    def __str__(self):
        return '{p}/{q}'.format(p=self.p, q=self.q)

    def __mul__(self, other):
        return Fraction(self.p * other.p, self.q * other.q)

    def __div__(self, other):
        return Fraction(self.p * other.q, self.q * other.p)

    def __rmul__(self, other):
        other_fraction = Fraction.from_decimal(other)
        return Fraction(self.p * other_fraction.p, self.q * other_fraction.q)

    def __add__(self, other):
        common_multiple = rational_math.lcm(self.q, other.q)
        self_multiplier = common_multiple / self.q
        other_multiplier = common_multiple / other.q
        return Fraction(self.p * self_multiplier +
                        other.p * other_multiplier, common_multiple)

    def __sub__(self, other):
        return self.__add__(-1.0 * other)

    def get_integer_part(self):
        return self.p / self.q

    def to_decimal(self):
        return self.p / float(self.q)

    def to_continuous(self):
        for quotient, remainder in rational_math.euclidean_algorithm(self.p,
                                                                     self.q):
            yield quotient

    def is_equal(self, p, q):
        return self.p == p and self.q == q

    @classmethod
    def is_fraction(cls, fraction_str):
        match = re.match(Fraction.FRACTION_REGEXP, fraction_str)
        return True if match else False

    @classmethod
    def get_nominator_denominator(cls, fraction_str):
        if Fraction.is_fraction(fraction_str):
            match = re.match(Fraction.FRACTION_REGEXP, fraction_str)
            return match.group(1), match.group(2)
        else:
            return None

    @classmethod
    def from_string(cls, fraction):
        if Fraction.is_fraction(fraction):
            p, q = Fraction.get_nominator_denominator(fraction)
            if not q:
                q = 1
            return Fraction(int(p), int(q))
