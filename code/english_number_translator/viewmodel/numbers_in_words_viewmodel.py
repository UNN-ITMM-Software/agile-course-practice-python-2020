from english_number_translator.logger.reallogger import RealLogger
from english_number_translator.model.translator import Translator
import re


class NumberInWordsViewModel:
    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.number = ''
        self.in_english = ''
        self.err_msg = ''
        self.button_enabled = 'disabled'
        self.logger.log('Starting...')

    def set_number_value(self, value):
        self.logger.log("Set number value to %s" % value)
        self.number = value.strip()
        self.validate_text()

    def set_in_english(self, value):
        self.logger.log("Set english number string to %s" % value)
        self.in_english = value

    def get_number_value(self):
        return self.number

    def get_in_english(self):
        return self.in_english

    def get_error_message(self):
        return self.err_msg

    def get_button_state(self):
        return self.button_enabled

    def validate_text(self):
        if self.err_msg != '':
            self.err_msg = ''

        if self.in_english != '':
            self.in_english = ''

        if re.match("\\d+$", str(self.number)):
            self.button_enabled = 'normal'
        else:
            if self.get_number_value() != '':
                self.err_msg = 'Only numbers'
            self.logger.log("Button was disabled")
            self.button_enabled = 'disabled'

    def click_convert(self):
        if self.button_enabled == 'normal':
            self.logger.log('Button was clicked')
            self.set_in_english(Translator.num_to_string(int(self.number)))
