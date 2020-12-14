from lcd_digits.model.lcd_digits_model import LcdDigitsModel


class LcdDigitViewModel:
    def __init__(self):
        self.message_text = ''
        self.digits = ''
        self.set_btn_disabled()

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_digits(self, value):
        self.digits = value.strip()
        self.validate_text()

    def get_digits(self):
        return self.digits

    def validate_text(self):
        if LcdDigitsModel.is_digit(self.digits):
            self.set_btn_enabled()
        else:
            self.set_btn_disabled()

    def set_btn_enabled(self):
        self.button_convert_state = 'normal'

    def set_btn_disabled(self):
        self.button_convert_state = 'disabled'

    def click_convert(self):
        lcd_digits = LcdDigitsModel(self.digits)

        self.message_text = LcdDigitViewModel.get_string(lcd_digits.lcd_numbers)

    def get_msg_text(self):
        return self.message_text

    @classmethod
    def get_string(cls, lcd_digits):
        result = ''
        for index in range(3):
            for lcd_digit in lcd_digits:
                result += lcd_digit.lcd_symbol[index] + ' '
            result += '\n'
        return result
