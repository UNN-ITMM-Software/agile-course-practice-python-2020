# noinspection PyPep8Naming
def GCD(p, q):
    if q == 0:
        return p
    else:
        return GCD(q, p % q)


# noinspection PyPep8Naming
def LCM(p, q):
    return p * q / GCD(p, q)
