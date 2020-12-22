import re


class LcdSymbol:
    """
    Класс переводящий отдельный символ в необходимое,
    согласно заданию, LCD представление
    """
    IS_SYMBOL = '^[0-9]$'

    MATCH_DICTIONARY = {
        '0': ['._.', '|.|', '|_|'],
        '1': ['...', '..|', '..|'],
        '2': ['._.', '._|', '|_.'],
        '3': ['._.', '._|', '._|'],
        '4': ['...', '|_|', '..|'],
        '5': ['._.', '|_.', '._|'],
        '6': ['._.', '|_.', '|_|'],
        '7': ['._.', '..|', '..|'],
        '8': ['._.', '|_|', '|_|'],
        '9': ['._.', '|_|', '..|']
    }

    lcd_symbol = []

    def __init__(self, symbol):
        if not re.fullmatch(LcdSymbol.IS_SYMBOL, symbol):
            raise ValueError('Match error: no symbol match')

        self.__symbol = symbol
        self.lcd_symbol = LcdSymbol.MATCH_DICTIONARY[symbol]

    def equals(self, obj):
        if not isinstance(obj, LcdSymbol):
            raise TypeError('Wrong type of obj. Expected: LcdSymbol')
        return self.__symbol == obj.__symbol and self.lcd_symbol == obj.lcd_symbol
