def euclide_algorithm(a, b):
    while b != 0:
        remainder = a % b
        quotinent = a / b
        a, b = b, remainder
        yield quotinent, remainder


# noinspection PyPep8Naming
def GCD(p, q):
    previous_remainder = q
    for quotinent, remainder in euclide_algorithm(p, q):
        if remainder != 0:
            previous_remainder = remainder
    return previous_remainder

# noinspection PyPep8Naming
def LCM(p, q):
    return p / GCD(p, q) * q
