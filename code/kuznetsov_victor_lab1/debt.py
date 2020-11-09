class DebtExpenses(object):
    def __init__(self, req_sum: int, percent_rate: float, period: int):
        if req_sum < 0 or percent_rate < 0 or period < 0:
            raise ValueError('Values must be positive numbers!')
        if not isinstance(req_sum, int) or not isinstance(period, int) or not isinstance(percent_rate, float):
            raise TypeError('Req. sum and period must be integer!')
        self.req_sum = req_sum
        self.percent_rate = percent_rate
        self.period = period

    def equal_amounts_repayment(self, year: int):
        if year < 1 or year > self.period:
            raise Exception('Year must be less than {}!'.format(self.period))

        expenses = self.req_sum / self.period
        percent_for_year = (self.req_sum - expenses * (year - 1)) * self.percent_rate
        payment = percent_for_year + expenses
        return payment, expenses

    def equal_payments_repayment(self, year: int):
        if year < 1 or year > self.period:
            raise Exception('Year must be less than {}!'.format(self.period))

        convertion_rate = (1 - (1 + self.percent_rate) ** (-self.period)) / self.percent_rate
        payment = self.req_sum / convertion_rate

        i = 0
        expenses = 0
        remaining = self.req_sum
        while i < year:
            expenses = payment - remaining * self.percent_rate
            remaining -= expenses
            i += 1

        return payment, expenses
