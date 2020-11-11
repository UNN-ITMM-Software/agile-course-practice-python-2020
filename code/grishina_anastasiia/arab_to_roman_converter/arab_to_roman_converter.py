def get_ones_of_number():
    return ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']


def get_tens_of_number():
    return ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]


def get_hundreds_of_number():
    return ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]


class ArabToRomanConverter:

    def __init__(self, number):
        self.number = number

    def convert_arab_to_roman_number(self):
        one = get_ones_of_number()[self.number % 10]
        ten = get_tens_of_number()[int(self.number / 10) % 10]
        hundred = get_hundreds_of_number()[int(self.number / 100) % 10]

        if self.number == 1000:
            return 'M'

        return hundred + ten + one
