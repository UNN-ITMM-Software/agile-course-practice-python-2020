from english_number_translator.model.translator import Translator
import re


class NumberInWordsViewModel:
    def __init__(self):
        self.number = ''
        self.in_english = ''
        self.err_msg = ''
        self.button_enabled = 'disabled'

    def set_number_value(self, value):
        self.number = value.strip()
        self.validate_text()

    def set_in_english(self, value):
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
            self.button_enabled = 'disabled'

    def click_convert(self):
        if self.button_enabled == 'normal':
            self.set_in_english(Translator.num_to_string(int(self.number)))
