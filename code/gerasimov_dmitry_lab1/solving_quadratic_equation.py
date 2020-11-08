def solving_quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError("The equation is not square. The first argument cannot be zero")
    if b == 0 and c == 0:
        return 0


