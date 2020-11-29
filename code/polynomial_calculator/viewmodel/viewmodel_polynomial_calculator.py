from polynomial_calculator.model.model_polynomial_calculator import check_zero, Polynomial


class PolyViewModel:
    def __init__(self):
        self.result = ''
        self.first_poly = ''
        self.second_poly = ''
        self.operation = '+'

    def set_first_poly(self, val):
        self.first_poly = val.strip()

    def set_second_poly(self, val):
        self.second_poly = val.strip()

    def set_operation(self, val):
        self.operation = val.strip()

    def get_result(self):
        return self.result

    def get_first_poly(self):
        return self.first_poly

    def get_second_poly(self):
        return self.second_poly

    def get_operation(self):
        return self.operation

    def computing(self):
        first_poly = Polynomial.from_string(self.first_poly)
        second_poly = Polynomial.from_string(self.second_poly)
        if first_poly and second_poly:
            if self.operation == '+':
                self.result = str(first_poly + second_poly)
            elif self.operation == '-':
                self.result = str(first_poly - second_poly)
            elif self.operation == '*':
                self.result = str(first_poly * second_poly)
        else:
            self.result = 'Coeff has no type int'
