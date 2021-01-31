from lcd_digits.model.lcd_digits_model import LcdDigitsModel
from lcd_digits.logger.log import Log_types


class LcdDigitViewModel:
    def __init__(self, logger):
        self.message_text = ''
        self.digits = ''
        self.logger = logger
        self.logger.add_log('LCD digit application is running.', Log_types.Info)
        self.set_btn_disabled()

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_digits(self, value):
        self.digits = value.strip()
        self.validate_text()
        self.logger.add_log('digits set = {}'.format(self.digits), Log_types.Info)

    def get_digits(self):
        return self.digits

    def validate_text(self):
        if LcdDigitsModel.is_digit(self.digits):
            self.set_btn_enabled()
        else:
            self.set_btn_disabled()

    def set_btn_enabled(self):
        self.logger.add_log('Button is enabled.', Log_types.Info)
        self.button_convert_state = 'normal'

    def set_btn_disabled(self):
        self.logger.add_log('Button is disabled.', Log_types.Info)
        self.button_convert_state = 'disabled'

    def click_convert(self, digit_number):
        self.logger.add_log('Button is clicked.', Log_types.Info)
        try:
            lcd_digits = LcdDigitsModel(self.digits)
            self.message_text = LcdDigitViewModel.get_string(lcd_digits.lcd_numbers, digit_number)
            self.logger.add_log('The answer:\n' + self.message_text, Log_types.Info)
        except ValueError as exception:
            self.logger.add_log(exception.__str__(), Log_types.Error)

    def get_msg_text(self):
        return self.message_text

    @classmethod
    def get_string(cls, lcd_digits, digit_number):
        result = ''
        for row_index in range(int(len(lcd_digits)*4 / digit_number) + 1):
            for index in range(3):
                for lcd_digit in lcd_digits[row_index * digit_number: (row_index+1) * digit_number]:
                    result += lcd_digit.lcd_symbol[index] + ' '
                if len(lcd_digits) > row_index * digit_number:
                    result += '\n'
        return result
