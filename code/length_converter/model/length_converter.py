from enum import Enum


class LengthConverter:

    def __init__(self, value, length_type):
        if float(value) < 0.0:
            raise ValueError
        self.value = float(value)
        self.length_type = length_type
        self.__length_type_coefficients = {
            LengthType.meter: 1.0,
            LengthType.centimeter: 100.0,
            LengthType.millimeter: 1000.0,
            LengthType.kilometer: 0.001
        }

    def __convert_self_to_meter(self):
        return self.value / self.__length_type_coefficients[self.length_type]

    def convert(self, to_length_type):
            return self.__convert_self_to_meter() * self.__length_type_coefficients[to_length_type]


class LengthType(Enum):
    meter = 0
    centimeter = 1
    millimeter = 2
    kilometer = 3
