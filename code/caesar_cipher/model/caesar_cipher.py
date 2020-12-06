import string


class CaesarCipher(object):
    def __init__(self, offset):
        self.alphabetVolume = string.ascii_lowercase.__len__()
        self.alphabet = {x: string.ascii_lowercase[x] for x in range(self.alphabetVolume)}
        self.letterMap = {string.ascii_lowercase[x]: x for x in range(self.alphabetVolume)}
        self.offset = offset % self.alphabetVolume

    def __convert_char__(self, char, offset):
        if not char.isalpha():
            return char
        flag = False
        if char.isupper():
            char = char.lower()
            flag = True
        res = self.alphabet[(self.letterMap[char] + offset) % self.alphabetVolume]
        if flag:
            return res.upper()
        return res

    def __convert_string__(self, message, offset):
        res = ""
        for char in message:
            res = res + self.__convert_char__(char, offset)
        return res

    def encode(self, message):
        return self.__convert_string__(message, self.offset)

    def decode(self, message):
        return self.__convert_string__(message, -self.offset)
