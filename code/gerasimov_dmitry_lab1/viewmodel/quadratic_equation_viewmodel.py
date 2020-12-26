from gerasimov_dmitry_lab1.solving_quadratic_equation import QuadraticEquation
from gerasimov_dmitry_lab1.logger.real_logger import RealLogger


class QuadraticEquationViewModel(object):
    button_enabled = 'disabled'
    result = None
    error_message = None
    qe = None

    def __init__(self, a=None, b=None, c=None, logger=RealLogger()):
        self.validate_input(a)
        self.a = a
        self.validate_input(b)
        self.b = b
        self.validate_input(c)
        self.c = c
        self.logger = logger
        self.logger.log('Welcome!')

    def is_button_enable(self):
        return self.button_enabled

    def validate_input(self, value):
        if isinstance(value, (int, float)) or isinstance(value, str) and value.isdigit():
            self.set_btn_enabled()
        else:
            self.set_btn_disabled()

    def set_a(self, value):
        self.validate_input(value)
        self.logger.log('Setting a = {}'.format(value))
        self.a = value

    def get_a(self):
        return self.a

    def set_b(self, value):
        self.validate_input(value)
        self.logger.log('Setting b = {}'.format(value))
        self.b = value

    def get_b(self):
        return self.b

    def set_c(self, value):
        self.validate_input(value)
        self.logger.log('Setting c = {}'.format(value))
        self.c = value

    def get_c(self):
        return self.c

    def set_btn_disabled(self):
        self.button_enabled = 'disabled'

    def set_btn_enabled(self):
        self.button_enabled = 'normal'

    def perform(self):
        if self.is_button_enable() == "normal":
            self.logger.log('Button clicked')
            try:
                self.qe = QuadraticEquation(float(self.a), float(self.b), float(self.c))
                self.result = self.qe.solution_in_string_format()
                self.clear_error_message()
                self.logger.log('a = {0}, b = {1}, c = {2}'.format(self.a, self.b, self.c))
                self.logger.log('Result = {}'.format(self.result))
            except Exception:
                self.clear_result()
                self.error_message = 'Incorrect input'
                self.logger.log(self.error_message)

    def get_result(self):
        return self.result

    def clear_result(self):
        self.result = None

    def get_error_message(self):
        return self.error_message

    def clear_error_message(self):
        self.error_message = None
