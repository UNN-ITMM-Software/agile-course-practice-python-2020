# noinspection PyPep8Naming
def GCD(p, q):
    if q == 0:
        return p
    else:
        return GCD(q, p % q)


# noinspection PyPep8Naming
def LCM(p, q):
    return p * q / GCD(p, q)


class Fraction:
    # The class represents rational number p/q, q!=0,
    # and the fraction is irreducible
    p = 0
    q = 1

    def __init__(self, p=0, q=1):
        common_divisor = GCD(p, q)
        self.p = p / common_divisor
        self.q = q / common_divisor

    def __mul__(self, other):
        return Fraction(self.p * other.p, self.q * other.q)

    def __add__(self, other):
        common_multiple = LCM(self.q, other.q)
        self_multiplier = common_multiple / self.q
        other_multiplier = common_multiple / other.q
        return Fraction(self.p * self_multiplier +
                        other.p * other_multiplier, common_multiple)
