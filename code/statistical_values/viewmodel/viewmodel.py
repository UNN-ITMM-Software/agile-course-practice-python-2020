from statistical_values.model.statistical_values import StatisticalValues
from statistical_values.logger.reallogger import RealLogger


class StatisticalValuesViewModel:
    def __init__(self, logger=RealLogger()):
        self.x = [0, 0, 0]
        self.k = 1
        self.x_in = str(self.x)
        self.k_in = str(self.k)
        self.button_state = "disabled"
        self.error_msg = ''
        self.statistic = None
        self.result = 0
        self.logger = logger
        self.logger.log('Welcome!')

    def get_button_state(self):
        return self.button_state

    def set_button_state(self, state):
        self.button_state = state

    def set_x(self, values):
        self.x_in = values
        is_valid = True
        try:
            values = eval(values)
            if isinstance(values, (list, tuple, int, float)):
                self.button_state = "active"
                self.error_msg = ''
            else:
                self.error_msg = "Error: only list or tuple input supported in Values List"
                self.button_state = "disabled"
                self.logger.log(self.error_msg)
                is_valid = False
        except Exception as exp:
            self.error_msg = "Error: incorrect expression in Values List"
            self.button_state = "disabled"
            self.logger.log(self.error_msg)
            is_valid = False

        if is_valid:
            self.x = values
            self.logger.log("Set x is {}.".format(values))
        return is_valid

    def get_x(self):
        return self.x_in

    def set_k(self, value):
        self.k_in = value
        is_valid = True
        try:
            value = eval(value)
            if isinstance(value, (int, float)):
                self.button_state = "active"
                self.error_msg = ''
            else:
                self.error_msg = "Error: only int or float input supported in k"
                self.button_state = "disabled"
                self.logger.log(self.error_msg)
                is_valid = False
        except Exception as exp:
            self.error_msg = "Error: incorrect value k"
            self.button_state = "disabled"
            self.logger.log(self.error_msg)
            is_valid = False

        if is_valid:
            self.k = value
            self.logger.log("Set k is {}.".format(value))
        return is_valid

    def get_k(self):
        return self.k_in

    def set_statistic(self, value):
        self.statistic = value
        self.logger.log("Set statistic is {}.".format(value))
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
            self.logger.log("Statistics with name `{}` was calculated. Result value is {}".format(
                self.statistic, self.result))
        except Exception as exp:
            self.error_msg = "Error: {}". format(exp)
            self.logger.log(self.error_msg)

    def get_result(self):
        return "Result: {}".format(self.result)

    def get_error_message(self):
        return self.error_msg
