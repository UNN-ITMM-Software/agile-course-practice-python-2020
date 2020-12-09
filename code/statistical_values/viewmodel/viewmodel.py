from statistical_values.model.statistical_values import StatisticalValues


class StatisticalValuesViewModel:
    def __init__(self):
        self.x = [0, 0, 0]
        self.k = 1
        self.x_in = str(self.x)
        self.k_in = str(self.k)
        self.button_state = "disabled"
        self.error_msg = ''
        self.statistic = None
        self.result = 0

    def get_button_state(self):
        return self.button_state

    def set_button_state(self, state):
        self.button_state = state

    def set_x(self, values):
        self.x_in = values
        self.x = values

    def get_x(self):
        return self.x_in

    def set_k(self, value):
        self.k_in = value
        self.k = value

    def get_k(self):
        return self.k_in

    def set_statistic(self, value):
        self.statistic = value
        if self.statistic is not None:
            self.button_state = 'active'

    def compute(self):
        try:
            calculator = StatisticalValues(self.x)
            if (self.statistic == 'mean'):
                self.result = calculator.mean()
            elif (self.statistic == 'variance'):
                self.result = calculator.variance()
            elif (self.statistic == 'median'):
                self.result = calculator.median()
            elif (self.statistic == 'begining moment'):
                self.result = calculator.begining_moment(self.k)
            elif (self.statistic == 'central moment'):
                self.result = calculator.central_moment(self.k)
        except Exception as exp:
            self.error_msg = "Error: {}". format(exp)

    def get_result(self):
        return "Result: {}".format(self.result)

    def get_error_message(self):
        return self.error_msg
