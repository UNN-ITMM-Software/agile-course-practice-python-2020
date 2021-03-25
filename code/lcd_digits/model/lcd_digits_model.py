from lcd_digits.model.lcd_symbol import LcdSymbol


class LcdDigitsModel:
    """
    Класс LcdDigitsModel
    Служит для перевода целых неотрицательных чисел
    в LCD Digit (каждая цифра от 0 до 9) представляет собой
    блок 3*3 где цифра отображается из 3 символов: . _ |
    """
    lcd_numbers = []

    def __init__(self, number_str):
        try:
            number = int(number_str)
            if number < 0:
                raise ValueError('Input error: wrong format')
            self.__number_str = number_str
            self.lcd_numbers = [LcdSymbol(symbol) for symbol in number_str]
        except ValueError:
            raise ValueError('Input error: wrong format')

    def equals(self, obj):
        if not isinstance(obj, LcdDigitsModel):
            raise TypeError('Wrong type of obj. Expected: LcdDigitsModel')
        result = self.__number_str == obj.__number_str
        result &= len(self.lcd_numbers) == len(obj.lcd_numbers)
        if result:
            for index in range(0, len(self.lcd_numbers)):
                result &= self.lcd_numbers[index].equals(obj.lcd_numbers[index])
        return result

    def __add__(self, other):
        new_number_str = self.__number_str + other.__number_str
        return LcdDigitsModel(new_number_str)

    @classmethod
    def is_digit(cls, digits_txt):
        return digits_txt.isdigit()
