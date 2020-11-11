from enum import Enum


class LengthConverter:

    def __init__(self, value, length_type):
        self.value = value
        self.length_type = length_type

    def convert(self, to_length_type):
        return 0


class LengthType(Enum):
    meter = 0
