from enum import Enum


class LengthConverter:

    def __init__(self, value, length_type):
        self.value = value
        self.length_type = length_type

    def convert(self, to_length_type):
        if self.length_type == to_length_type:
            return self.value


class LengthType(Enum):
    meter = 0
