import re


class ViewModel:
    def __init__(self):
        self.set_btn_disabled()
        self.first_fraction = ''
        self.second_fraction = ''

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_button_convert_state(self, state):
        self.button_convert_state = state

    def set_second_fraction(self, value):
        self.second_fraction = value.strip()
        self.validate_text()

    def is_fraction(self, fraction):
        if re.match('^\d+(?:[/]\d+)?$', fraction):
            return True
        else:
            return False

    def validate_text(self):
        is_first_fraction = self.is_fraction(self.first_fraction)
        is_second_fraction = self.is_fraction(self.second_fraction)
        if is_first_fraction and is_second_fraction:
            self.set_btn_enabled()
        else:
            self.set_btn_disabled()

    def set_btn_enabled(self):
        self.button_convert_state = 'normal'

    def set_btn_disabled(self):
        self.button_convert_state = 'disabled'

    def get_second_fraction(self):
        return self.second_fraction

    def set_first_fraction(self, value):
        self.first_fraction = value.strip()
        self.validate_text()

    def get_first_fraction(self):
        return self.first_fraction
