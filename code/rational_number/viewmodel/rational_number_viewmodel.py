import re

class RationalNumberViewModel:

    def __init__(self):
        self.__first_number = ""
        self.__second_number = ""
        self.__calculate_button_state = "disabled"
        self._info_message = ""

    def is_number_valid(self, value):
        return re.match(r"\d+\/\d+", value)

    def validate_input_numbers(self):
        first_number_valid = self.is_number_valid(self.__first_number)
        second_number_valid = self.is_number_valid(self.__second_number)

        if first_number_valid and second_number_valid:
            self.enable_calculate_button()
        else:
            self.disable_calculate_button()

    def enable_calculate_button(self):
        self.__calculate_button_state = "normal"

    def disable_calculate_button(self):
        self.__calculate_button_state = "disabled"

    def get_calculate_button_state(self):
        return self.__calculate_button_state

    def set_first_number(self, value):
        self.__first_number = value.strip()
        self.validate_input_numbers()

    def set_second_number(self, value):
        self.__second_number = value.strip()
        self.validate_input_numbers()
