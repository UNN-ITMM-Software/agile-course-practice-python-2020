class RationalNumber:
    def __init__(self, numerator, denominator):
        if type(numerator) != int or type(denominator) != int:
            raise TypeError
        if denominator == 0:
            raise ZeroDivisionError
        self._num = numerator
        self._den = denominator
        self._reduce()

    def _reduce(self):
        gcd = self._gcd(max(self._num, self._den), min(self._num, self._den))
        self._num //= gcd
        self._den //= gcd
        if self._den < 0:
            self._den *= -1
            self._num *= -1

    def _gcd(self, a, b):
        return a if b == 0 else self._gcd(b, a % b)

    def __eq__(self, other):
        return self._den == other._den and self._num == other._num

    def __str__(self):
        if self._den == 1:
            return str(self._num)
        return str(self._num) + '/' + str(self._den)

    def __add__(self, other):
        return RationalNumber(self._num*other._den+self._den*other._num, self._den*other._den)

    def __neg__(self):
        return RationalNumber(-self._num, self._den)
