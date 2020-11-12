class NumericalIntegrator(object):
    N = 1000
    def trapeziumMethod(self, a, b, func):
        width = (b - a) / self.N
        trapezoidalIntegral = 0
        for i in range(self.N): 
            x1 = a + i * width;
            x2 = a + (i + 1) * width;
            trapezoidalIntegral += 0.5 * (x2 - x1) * (func(x1) + func(x2))
        return trapezoidalIntegral
    
    def simpsonMethod(self, a, b, func):
        width = (b - a) / self.N
        simpsonIntegral = 0
        for i in range(self.N): 
            x1 = a + i * width;
            x2 = a + (i + 1) * width;
            simpsonIntegral += (x2 - x1) / 6.0 * (func(x1) + 4.0 * func(0.5 * (x1 + x2)) + func(x2))
        return simpsonIntegral