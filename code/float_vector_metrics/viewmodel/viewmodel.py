from float_vector_metrics.model.float_vector_metrics import VectorMetrics


class VectorMetricsViewModel:
    calculator = VectorMetrics()
    METRICS = {
    'L1': calculator.l1,
    'L2': calculator.l2,
    'L3': calculator.l3,
    'L4': calculator.l4,
    'Linf': calculator.linf
}
    def __init__(self):
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
                self.button_state = "disabled"
                return False
        except Exception as exp:
            self.error_msg = "Error: Incorrect expression, only list notations supported"
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
        return is_valid

    def get_x(self):
        return self.x_in

    def set_y(self, value):
        self.y_in = value
        is_valid = self.validate(value)
        if is_valid:
            self.y = eval(value)
        return is_valid

    def get_y(self):
        return self.y_in

    def get_error_message(self):
        return self.error_msg

    def set_metric(self, value):
        self.metric = self.METRICS.get(value, None)
        if self.metric is not None:
            self.button_state = 'active'

    def compute(self):
        try:
            self.result = self.metric(self.x, self.y)
        except Exception as exp:
            self.error_msg = "Error: {}". format(exp)

    def get_result(self):
        return "Result: {}".format(self.result)
