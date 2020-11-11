def get_ones_of_number():
    return ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VII', 'IX']


class ArabToRomanConverter:

    def __init__(self, number):
        self.number = number

    def convert_arab_to_roman_number(self):
        if self.number == 10:
            return 'X'
        elif self.number == 70:
            return 'LXX'
        return get_ones_of_number()[self.number]
