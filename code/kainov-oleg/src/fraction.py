# noinspection PyPep8Naming
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


class Fraction:
    # The class represents rational number p/q, q!=0,
    # and the fraction is irreducible
    p = 0
    q = 1

    def __init__(self, p=0, q=1):
        self.p = p
        self.q = q
