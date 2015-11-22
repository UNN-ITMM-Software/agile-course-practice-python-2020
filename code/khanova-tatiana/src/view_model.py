from model.color_space import ColorSpace
from model.color import Color
from model.color_space_converter import ColorSpaceConverter
import numpy as np
import operator


class ViewModel:
    @staticmethod
    def is_correct(color):
        # if map(str.isdigit, color) == [True] * 3:
        # print map(operator.methodcaller("isdigit"), color)
        if map(operator.methodcaller("isdigit"), color) == [True] * 3:
            return True
        else:
            return False

    def __init__(self):
        self.error_message_text = ''
        self.color_space_in = "RGB"
        self.color_space_out = "RGB"
        self.color_in = ['0', '0', '0']
        self.color_out = ['', '', '']
        self.button_convert_state = "enabled"
        self.converter = ColorSpaceConverter()

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_button_convert_state(self, state):
        self.button_convert_state = state

    def set_color_space_in(self, color_space):
        self.color_space_in = color_space
        self.error_message_text = ""
        if color_space not in ColorSpace.SUPPORTED_COLOR_SPACES:
            self.error_message_text = "Unsupported color space."
            self.set_button_convert_state("disabled")

    def set_color_space_out(self, color_space):
        self.color_space_out = color_space
        self.error_message_text = ""
        if color_space not in ColorSpace.SUPPORTED_COLOR_SPACES:
            self.error_message_text = "Unsupported color space."
            self.set_button_convert_state("disabled")

    def set_color_in(self, color):
        self.color_in = color
        self.error_message_text = ""
        if ViewModel.is_correct(color):
            if len(color) == len([val for val in map(int, color) if val <= 255 and val >= 0]):
                self.color_in = color
                self.set_button_convert_state("enabled")
                return
            else:
                self.error_message_text = "Input values should be in range 0-255."
        else:
            self.error_message_text = "Incorrect values."

        self.set_button_convert_state("disabled")

    def get_color_space_out(self):
        return self.color_space_out

    def get_color_space_in(self):
        return self.color_space_in

    def get_color_out(self):
        return self.color_out

    def get_color_in(self):
        return self.color_in

    def convert(self):
        color = Color(ColorSpace(self.color_space_in), np.array(map(int, self.color_in)))
        converted_color = self.converter.convert(color, ColorSpace(self.color_space_out))
        self.color_out = map(str, converted_color.value.tolist())

    def get_error_message(self):
        return self.error_message_text
