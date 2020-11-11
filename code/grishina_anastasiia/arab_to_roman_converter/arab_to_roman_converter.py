def get_ones_of_number():
    return ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']


def get_tens_of_number():
    return ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]


def get_hundreds_of_number():
    return ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]


def get_thousand_of_number(count):
    res = ''
    for num in range(count):
        res += 'M'
    return res


def get_arab_to_roman_map():
    return {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }


class ArabToRomanConverter:

    def __init__(self, number):
        self.number = number

    def convert_arab_to_roman_number(self):
        one = get_ones_of_number()[self.number % 10]
        ten = get_tens_of_number()[int(self.number / 10) % 10]
        hundred = get_hundreds_of_number()[int(self.number / 100) % 10]
        thousand = get_thousand_of_number(int(self.number / 1000) % 10)

        return thousand + hundred + ten + one

    def convert_roman_to_arab_number(self):
        numbers = list(self.number)
        result = 0
        i = 0
        roman_numbers = []
        for number in numbers:
            roman_numbers.append(float(get_arab_to_roman_map()[number]))

        while i < len(roman_numbers) - 1:
            if roman_numbers[i] < roman_numbers[i + 1]:
                result -= roman_numbers[i]
            else:
                result += roman_numbers[i]
            i += 1

        result += roman_numbers[len(roman_numbers) - 1]
        return result
