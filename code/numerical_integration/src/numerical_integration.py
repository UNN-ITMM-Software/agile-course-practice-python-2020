class NumericalIntegrator(object):
    N = 1000

    def trapezium_method(self, a, b, func):
        width = (b - a) / self.N
        trapezoidal_integral = 0
        for i in range(self.N):
            x1 = a + i * width
            x2 = a + (i + 1) * width
            trapezoidal_integral += 0.5 * (x2 - x1) * (func(x1) + func(x2))
        return trapezoidal_integral

    def simpson_method(self, a, b, func):
        width = (b - a) / self.N
        simpson_integral = 0
        for i in range(self.N):
            x1 = a + i * width
            x2 = a + (i + 1) * width
            simpson_integral += (x2 - x1) / 6.0 * (func(x1) + 4.0 * func(0.5 * (x1 + x2)) + func(x2))
        return simpson_integral
