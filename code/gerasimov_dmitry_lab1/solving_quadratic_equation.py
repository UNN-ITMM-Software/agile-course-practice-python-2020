import math

NO_SOLUTION = "No solution"


def solving_quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError("The equation is not square. The first argument cannot be zero")
    disc = b ** 2 - 4 * a * c
    if b == 0:
        if c == 0:
            disc = 0
        elif a > 0 and c > 0 or a < 0 and c < 0:
            return NO_SOLUTION

    if disc < 0:
        return NO_SOLUTION
    elif disc == 0:
        x = (-b / (2 * a))
        return x
    else:
        x1 = (-b + math.sqrt(disc)) / (2 * a)
        x2 = (-b - math.sqrt(disc)) / (2 * a)
        res = sorted([x1, x2])
    return res[0], res[1]
