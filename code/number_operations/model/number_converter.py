class Converter():
    def __init__(self, number, base):
        self.number = 0
        self.base = base
        for char in number:
            val = self.__char_to_digit(char)
            if val >= base:
                raise ValueError('Found digit outside base!')

            self.number *= base
            self.number += val

    def convert(self, base):
        result = []
        integer = self.number
        while integer:
            integer, value = divmod(integer, base)
            result.append(self.__digit_to_char(value))
        return ''.join(reversed(result))

    def __char_to_digit(self, char):
        try:
            return int(char)
        except:
            if (ord(char) < ord('a')):
                raise ValueError('Invalid character!')
            return ord(char) - ord('a') + 10

    def __digit_to_char(self, digit):
        if digit < 10:
            return str(digit)
        return chr(ord('a') + digit - 10)
