class BigInteger(object):
    BASE = 10
    SIZE = 100

    def __init__(self, digits=[]):
        self.digits = [0 for i in range(self.SIZE)]
        for i in range(len(digits)):
            self.digits[i] = digits[i]

    def __eq__(self, other):
        for i in range(self.SIZE):
            if self.digits[i] != other.digits[i]:
                return False
        return True

    def __add__(self, other):
        result = BigInteger()
        for i in range(self.SIZE):
            result.digits[i] = self.digits[i] + other.digits[i]
        for i in range(self.SIZE - 1):
            if result.digits[i] >= self.BASE:
                result.digits[i] -= self.BASE
                result.digits[i + 1] += 1
        return result

    def __sub__(self, other):
        result = BigInteger()
        for i in range(self.SIZE):
            result.digits[i] = self.digits[i] - other.digits[i]
        for i in range(self.SIZE - 1):
            if result.digits[i] < 0:
                result.digits[i] += self.BASE
                result.digits[i + 1] -= 1
        return result

    def __mul__(self, other):
        result = BigInteger()
        for i in range(self.SIZE):
            for j in range(self.SIZE - i):
                result.digits[i + j] += self.digits[i] * other.digits[j]
        for i in range(self.SIZE - 1):
            result.digits[i + 1] += result.digits[i] // self.BASE
            result.digits[i] %= self.BASE
        return result
