import re


class VigenereCipher:
    def __init__(self, key="key"):
        self.key = ""
        if not isinstance(key, str):
            raise TypeError("The key type must be 'string'")
        for k in key:
            if not re.search(r'[^a-zA-Z]', k):
                self.key += k.lower()
        if not self.key:
            raise ValueError("The key must be letters and not empty")
