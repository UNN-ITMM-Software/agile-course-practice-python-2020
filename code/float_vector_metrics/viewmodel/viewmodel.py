from float_vector_metrics.model.float_vector_metrics import VectorMetrics

from float_vector_metrics.logger.fakelogger import FakeLogger


class VectorMetricsViewModel:
    calculator = VectorMetrics()
    METRICS = {
        'L1': calculator.l1,
        'L2': calculator.l2,
        'L3': calculator.l3,
        'L4': calculator.l4,
        'Linf': calculator.linf
    }

    def __init__(self, logger=FakeLogger()):
        self.logger = logger
        self.logger.log('Welcome to The Float Vector Metrics Calculator!')
        self.x = [0, 0, 0]
        self.y = [0, 0, 0]
        self.x_in = str(self.x)
        self.y_in = str(self.y)
        self.button_state = "disabled"
        self.result = 0
        self.error_msg = ''
        self.metric = None

    def validate(self, value):
        try:
            value = eval(value)
            if isinstance(value, list):
                self.button_state = "active"
                self.error_msg = ''
                return True
            else:
                self.error_msg = "Error: Only list notations supported"
                self.logger.log('%s' % self.error_msg)
                self.button_state = "disabled"
                return False
        except Exception as exp:
            self.error_msg = "Error: Incorrect expression, only list of float or int values supported"
            self.logger.log('%s' % self.error_msg)
            self.button_state = "disabled"
            return False

    def get_button_state(self):
        return self.button_state

    def set_button_state(self, state):
        self.button_state = state

    def set_x(self, value):
        self.x_in = value
        is_valid = self.validate(value)
        if is_valid:
            self.x = eval(value)
            self.logger.log('Setting x vector to %s' % self.x_in)
        return is_valid

    def get_x(self):
        return self.x_in

    def set_y(self, value):
        self.y_in = value
        is_valid = self.validate(value)
        if is_valid:
            self.y = eval(value)
            self.logger.log('Setting y vector to %s' % self.y_in)
        return is_valid

    def get_y(self):
        return self.y_in

    def get_error_message(self):
        return self.error_msg

    def set_metric(self, value):
        self.metric = self.METRICS.get(value, None)
        self.logger.log('Setting metric to %s' % value)
        if self.metric is not None and self.error_msg == '':
            self.button_state = 'active'

    def compute(self):
        self.logger.log('Button clicked')
        try:
            self.result = self.metric(self.x, self.y)
            self.logger.log('Result: %s' % self.result)
        except Exception as exp:
            self.error_msg = "Error: {}". format(exp)
            self.logger.log('%s' % self.error_msg)

    def get_result(self):
        return "Result: {}".format(self.result)
