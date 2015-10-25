# noinspection PyPep8Naming
def GCD(p, q):
    while q != 0:
        p = p % q
        p, q = q, p
    return p

# noinspection PyPep8Naming
def LCM(p, q):
    return p * q / GCD(p, q)
