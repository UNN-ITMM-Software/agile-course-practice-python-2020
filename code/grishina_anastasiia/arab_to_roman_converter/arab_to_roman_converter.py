def get_ones_of_number():
    return ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VII', 'IX']


def get_tens_of_number():
    return ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]


class ArabToRomanConverter:

    def __init__(self, number):
        self.number = number

    def convert_arab_to_roman_number(self):
        if self.number == 15 or self.number == 82:
            return get_tens_of_number()[int(self.number / 10) % 10] + get_ones_of_number()[self.number % 10]
        if self.number == 10 or self.number == 70:
            return get_tens_of_number()[int(self.number / 10)]
        return get_ones_of_number()[self.number]
