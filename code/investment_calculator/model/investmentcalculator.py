
class InvalidFormulaError(Exception):
    pass

class InvestmentCalculator:
    def __init__(self, R=1, K=1, n=1, q=1):
        if isinstance(R, bool) or isinstance(K, bool) \
                or isinstance(n, bool) or isinstance(q, bool):
            raise InvalidFormulaError('invalid data type')
        if isinstance(R, (int, float)) and isinstance(K, (int, float)) \
                and isinstance(n, (int, float)) and isinstance(q, (int, float)):
            if R < 0 or K < 0 or n < 0 or q <= 0:
                raise InvalidFormulaError('values cannot be less than 0')
        else:
            raise InvalidFormulaError('invalid data type')
        self.R = R  # annual income
        self.K = K  # size of investment
        self.n = n  # number of years
        self.q = q  # comparison rate

    def add_R(self, R):
        self.R = R  # annual income

    def add_K(self, K):
        self.K = K  # size of investment

    def add_n(self, n):
        self.n = n  # number of years

    def add_q(self, q):
        self.q = q  # comparison rate

    def calculate_net_present_value(self):
        return self.R*(1-(1+self.q)**(-self.n))/self.q-self.K
