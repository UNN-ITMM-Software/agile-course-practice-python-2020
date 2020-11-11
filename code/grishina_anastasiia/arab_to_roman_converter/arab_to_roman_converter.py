class ArabToRomanConverter:

    def __init__(self, number):
        self.number = number

    def convert_arab_to_roman_number(self):
        if self.number == 1:
            return 'I'
        elif self.number == 2:
            return 'II'
        elif self.number == 5:
            return 'V'
