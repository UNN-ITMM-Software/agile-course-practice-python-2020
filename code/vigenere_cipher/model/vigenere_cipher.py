import re


class VigenereCipher:
    def __init__(self, key=""):
        self.key = ""
        if not isinstance(key, str):
            raise TypeError("The key type must be 'string'")
        for k in key:
            if re.search(r'[^a-zA-Z]', k):
                self.key += k.lower()
