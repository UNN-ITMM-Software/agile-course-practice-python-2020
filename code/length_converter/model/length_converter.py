from enum import Enum


class LengthConverter:

    def __init__(self, value, length_type):
        self.value = value
        self.length_type = length_type
        self.__length_type_coefficients = {
            LengthType.meter: 1,
            LengthType.centimeter: 100,
        }

    def convert(self, to_length_type):
            return self.value * self.__length_type_coefficients[to_length_type]


class LengthType(Enum):
    meter = 0
    centimeter = 1
