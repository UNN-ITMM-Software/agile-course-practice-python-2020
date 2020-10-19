def euclidean_algorithm(a, b):
    while b != 0:
        remainder = a % b
        quotient = int(a / b)
        a, b = b, remainder
        yield quotient, remainder

def gcd(p, q):
    previous_remainder = q
    for quotient, remainder in euclidean_algorithm(p, q):
        if remainder != 0:
            previous_remainder = remainder
    return previous_remainder

def lcm(p, q):
    return p / gcd(p, q) * q
