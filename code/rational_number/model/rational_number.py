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
        if self._den < 0:
            self._den *= -1
            self._num *= -1

    def __eq__(self, other):
        return self._den == other._den and self._num == other._num
