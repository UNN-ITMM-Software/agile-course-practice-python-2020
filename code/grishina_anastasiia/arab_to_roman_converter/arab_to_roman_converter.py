def get_ones_of_number():
    return ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VII', 'IX']


def get_tens_of_number():
    return ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]


class ArabToRomanConverter:

    def __init__(self, number):
        self.number = number

    def convert_arab_to_roman_number(self):
        if self.number == 100:
            return 'C'

        one = get_ones_of_number()[self.number % 10]
        ten = get_tens_of_number()[int(self.number / 10) % 10]
        return ten + one
