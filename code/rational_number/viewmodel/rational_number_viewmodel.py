import re

class RationalNumberViewModel:

    def __init__(self):
        self.__first_number = ""
        self.__second_number = ""
        self.__calculate_button_state = "disabled"
        self.__info_message = ""

    @staticmethod
    def is_number_valid(value):
        return re.match(r"\d+\/\d+", value)

    def validate_input_numbers(self):
        first_info = ""
        second_info = ""

        first_number_valid = self.is_number_valid(self.__first_number)
        second_number_valid = self.is_number_valid(self.__second_number)

        if first_number_valid and second_number_valid:
            self.enable_calculate_button()
        else:
            if not self.__first_number:
                first_info = "First number is empty."
            elif not first_number_valid:
                first_info = "First number is invalid."

            if not self.__second_number:
                second_info = "Second number is empty."
            elif not second_number_valid:
                second_info = "Second number is invalid."

            self.disable_calculate_button()

        self.__info_message = first_info + second_info

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

    def get_info_message(self):
        return self.__info_message
