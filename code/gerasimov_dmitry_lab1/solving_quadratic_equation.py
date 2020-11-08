import math

NO_SOLUTION = "No solution"


def solving_quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError("The equation is not square. The first argument cannot be zero")
    discr = b ** 2 - 4 * a * c
    if b == 0:
        if c == 0:
            discr = 0
        elif a > 0 and c > 0 or a < 0 and c < 0:
            return NO_SOLUTION

    if discr < 0:
        return NO_SOLUTION

    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)

    if x1 == x2:
        if x1 == 0:
            return 0
        else:
            return x1
    res = sorted([x1, x2])
    return res[0], res[1]

