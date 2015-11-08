
class ViewModel:
    def __init__(self):
        self.button_convert_state = 'disabled'
        self.first_fraction = ''
        self.second_fraction = ''

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_button_convert_state(self, state):
        self.button_convert_state = state

    def set_second_fraction(self, value):
        self.second_fraction = value.strip()
        if self.first_fraction and self.second_fraction:
            self.button_convert_state = 'normal'

    def get_second_fraction(self):
        return self.second_fraction

    def set_first_fraction(self, value):
        self.first_fraction = value.strip()
        if self.first_fraction and self.second_fraction:
            self.button_convert_state = 'normal'

    def get_first_fraction(self):
        return self.first_fraction
