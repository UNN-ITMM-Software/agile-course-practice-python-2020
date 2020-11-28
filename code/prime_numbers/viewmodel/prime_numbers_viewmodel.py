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

    def __init__(self, start=None, end=None):
        self.start_value = start
        self.end_value = end
        self.validate_values()

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
        self.start_value = value
        self.validate_values()

    def get_start_value(self):
        return self.start_value

    def get_end_value(self):
        return self.end_value

    def set_end_value(self, value):

        self.end_value = value
        self.validate_values()

    def set_btn_disabled(self):
        self.button_enabled = 'disabled'

    def set_btn_enabled(self):
        self.button_enabled = 'normal'

    def perform(self):
        if self.is_button_enable() == "normal":
            try:
                self.interval = Range(int(self.start_value), int(self.end_value))
                self.result = get_primers(self.interval)
                self.clear_error_message()
            except Exception:
                self.clear_result()
                self.error_message = 'Что-то пошло не так.\nВозможно первое число оказалось больше второго'

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
