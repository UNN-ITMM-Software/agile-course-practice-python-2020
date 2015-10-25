def euclidean_algorithm(a, b):
    while b != 0:
        remainder = a % b
        quotient = a / b
        a, b = b, remainder
        yield quotient, remainder


# noinspection PyPep8Naming
def GCD(p, q):
    previous_remainder = q
    for quotient, remainder in euclidean_algorithm(p, q):
        if remainder != 0:
            previous_remainder = remainder
    return previous_remainder


# noinspection PyPep8Naming
def LCM(p, q):
    return p / GCD(p, q) * q
