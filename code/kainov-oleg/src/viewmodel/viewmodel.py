from model.fraction import Fraction, InvalidFractionError


class ViewModel:
    def __init__(self):
        self.message_text = ''
        self.set_btn_disabled()
        self.first_fraction = ''
        self.second_fraction = ''
        self.operation = '+'
        self.set_btn_disabled()
        self.set_second_fraction_text_enabled()

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_second_fraction(self, value):
        self.second_fraction = value.strip()
        self.validate_text()

    def validate_text(self):
        is_first_fraction = Fraction.is_fraction(self.first_fraction)
        is_second_fraction = Fraction.is_fraction(self.second_fraction)
        if is_first_fraction and is_second_fraction:
            self.set_btn_enabled()
        else:
            self.set_btn_disabled()

    def set_btn_enabled(self):
        self.button_convert_state = 'normal'

    def set_btn_disabled(self):
        self.button_convert_state = 'disabled'

    def set_second_fraction_text_enabled(self):
        self.second_fraction_text_state = 'normal'

    def set_second_fraction_text_disabled(self):
        self.second_fraction_text_state = 'disabled'

    def get_second_fraction(self):
        return self.second_fraction

    def set_first_fraction(self, value):
        self.first_fraction = value.strip()
        self.validate_text()

    def get_first_fraction(self):
        return self.first_fraction

    def click_convert(self):
        if self.operation == '+':
            self.message_text = str(Fraction.from_string(self.first_fraction) +
                                    Fraction.from_string(self.second_fraction))
        elif self.operation == '-':
            self.message_text = str(Fraction.from_string(self.first_fraction) -
                                    Fraction.from_string(self.second_fraction))
        elif self.operation == '*':
            self.message_text = str(Fraction.from_string(self.first_fraction) *
                                    Fraction.from_string(self.second_fraction))
        elif self.operation == '/':
            try:
                result = Fraction.from_string(self.first_fraction) / \
                    Fraction.from_string(self.second_fraction)
            except InvalidFractionError:
                result = 'Error! Cannot divide by zero!'
            self.message_text = str(result)
        else:
            self.message_text = str(list(
                Fraction.from_string(self.first_fraction).to_continuous()))

    def get_msg_text(self):
        return self.message_text

    def set_operation(self, operation):
        self.operation = operation
        if operation == 'Convert to continuous':
            self.set_second_fraction_text_disabled()
        else:
            self.set_second_fraction_text_enabled()

    def get_second_fraction_text_state(self):
        return self.second_fraction_text_state
