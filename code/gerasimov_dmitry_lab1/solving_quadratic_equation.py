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
    return discr

