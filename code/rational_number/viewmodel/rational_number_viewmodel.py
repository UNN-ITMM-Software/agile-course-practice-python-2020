import re
from rational_number.model.rational_number import RationalNumber


class RationalNumberViewModel:
    VALID_OPERATIONS = ['+', '-', '*', '/']

    def __init__(self):
        self.__first_number = ""
        self.__second_number = ""
        self.__operation = RationalNumberViewModel.VALID_OPERATIONS[0]
        self.__calculate_button_state = "disabled"
        self.__info_message = ""
        self.__result = ""

    @staticmethod
    def is_number_valid(value):
        return re.match(r"(-)?\d+\/(-)?\d+", value)

    def validate_input(self):
        self.__info_message = self.validate_operation() + self.validate_input_numbers()

        if not self.__info_message:
            self.enable_calculate_button()
        else:
            self.disable_calculate_button()

    def validate_operation(self):
        operation_message = ""

        if self.__operation not in self.VALID_OPERATIONS:
            operation_message = "Operation is invalid."
        return operation_message

    def validate_input_numbers(self):
        first_info = ""
        second_info = ""

        first_number_valid = self.is_number_valid(self.__first_number)
        second_number_valid = self.is_number_valid(self.__second_number)

        if not self.__first_number:
            first_info = "First number is empty."
        elif not first_number_valid:
            first_info = "First number is invalid."

        if not self.__second_number:
            second_info = "Second number is empty."
        elif not second_number_valid:
            second_info = "Second number is invalid."

        return first_info + second_info

    def enable_calculate_button(self):
        self.__calculate_button_state = "normal"

    def disable_calculate_button(self):
        self.__calculate_button_state = "disabled"

    def get_calculate_button_state(self):
        return self.__calculate_button_state

    def set_first_number(self, value):
        self.__first_number = value.strip()
        self.validate_input()

    def set_second_number(self, value):
        self.__second_number = value.strip()
        self.validate_input()

    def set_operation(self, value):
        self.__operation = value.strip()
        self.validate_input()

    def get_info_message(self):
        return self.__info_message
