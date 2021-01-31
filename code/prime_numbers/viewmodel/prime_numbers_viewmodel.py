from prime_numbers.logger.reallogger import RealLogger

from prime_numbers.model.prime_numbers import get_primers, Range
import re


def is_number_entered(value):
    if value is None or len(str(value).strip()) == 0:
        return False
    else:
        is_int_value = re.match("\\d+$", str(value))
        if is_int_value is None:
            return False
        else:
            return True


class PrimeNumberViewModel:
    button_enabled = 'disabled'
    result = None
    error_message = None
    interval = None

    def __init__(self, start=None, end=None, logger=RealLogger()):
        self.start_value = start
        self.end_value = end
        self.validate_values()
        self.logger = logger
        self.logger.log('Welcome!')

    def is_button_enable(self):
        return self.button_enabled

    def validate_values(self):
        is_start_exist = is_number_entered(self.start_value)
        is_end_exist = is_number_entered(self.end_value)

        if is_start_exist and is_end_exist:
            self.set_btn_enabled()
        else:
            self.set_btn_disabled()

    def set_start_value(self, value):
        if self.start_value != value:
            self.start_value = value
            self.logger.log('Setting start value - %s' % self.start_value)
            self.validate_values()

    def get_start_value(self):
        return self.start_value

    def get_end_value(self):
        return self.end_value

    def set_end_value(self, value):
        if self.end_value != value:
            self.end_value = value
            self.logger.log('Setting end value - %s' % self.end_value)
            self.validate_values()

    def set_btn_disabled(self):
        self.button_enabled = 'disabled'

    def set_btn_enabled(self):
        self.button_enabled = 'normal'

    def perform(self):
        if self.is_button_enable() == "normal":
            self.logger.log('Button clicked')
            try:
                self.interval = Range(int(self.start_value), int(self.end_value))
                self.result = get_primers(self.interval)
                self.clear_error_message()
                self.logger.log('Interval = %s' % self.interval)
                self.logger.log('Result = %s' % self.result)
            except Exception:
                self.clear_result()
                self.error_message = 'Что-то пошло не так.\nВозможно первое число оказалось больше второго'
                self.logger.log(str(self.error_message))

    def get_result(self):
        return self.result

    def clear_result(self):
        self.result = None

    def get_error_message(self):
        return self.error_message

    def clear_error_message(self):
        self.error_message = None

    def get_interval_label(self):
        return str(self.interval) if self.interval is not None else ''
