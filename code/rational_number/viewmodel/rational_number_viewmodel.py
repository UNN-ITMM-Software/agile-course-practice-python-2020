

class RationalNumberViewModel:

    def __init__(self):
        self.__first_number = ""
        self.__second_number = ""
        self.__calculate_button_state = "disabled"

    def validate_input_numbers(self):
        print(self.__first_number, self.__second_number)
        if self.__first_number and self.__second_number:
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
