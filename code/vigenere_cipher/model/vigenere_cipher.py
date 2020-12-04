import re


def check(string, key):
    if not isinstance(string, str):
        raise TypeError("only string")
    if not isinstance(key, str):
        raise TypeError("The key type must be 'string'")
    if len(key) == 0:
        raise ValueError("The key must be not empty")
    if re.search(r'[^A-Z]', key):
        raise ValueError("The key must be letters")


class VigenereCipher:
    def __init__(self, key="key"):
        self.key = ""
        if not isinstance(key, str):
            raise TypeError("The key type must be 'string'")
        for k in key:
            if not re.search(r'[^a-zA-Z]', k):
                self.key += k.upper()
        if not self.key:
            raise ValueError("The key must be letters and not empty")

    def a2i(self, ch):
        if not isinstance(ch, str):
            raise TypeError("The letter to number")
        if len(ch) != 1:
            raise ValueError("Just one letter")
        ch = ch.upper()
        if re.search(r'[^A-Z]', ch):
            raise ValueError("English alphabet")
        arr = {'A': 0,  'B': 1,  'C': 2,  'D': 3,  'E': 4,  'F': 5,  'G': 6,  'H': 7,  'I': 8,
               'J': 9,  'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
               'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
        return arr[ch]

    def i2a(self, i):
        if not isinstance(i, int):
            raise TypeError("The number to letter")
        i = i % 26
        arr = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        return arr[i]

    def encipher(self, string):
        check(string, self.key)
        res = ""
        i = 0
        for c in string:
            c = c.upper()
            j = i % len(self.key)
            if re.search(r'[^A-Z]', c):
                res += c
            else:
                res += self.i2a(self.a2i(c) + self.a2i(self.key[j]))
                i += 1
        return res

    def decipher(self, string):
        check(string, self.key)
        res = ""
        i = 0
        for c in string:
            c = c.upper()
            j = i % len(self.key)
            if re.search(r'[^A-Z]', c):
                res += c
            else:
                res += self.i2a(self.a2i(c) - self.a2i(self.key[j]))
                i += 1
        return res
