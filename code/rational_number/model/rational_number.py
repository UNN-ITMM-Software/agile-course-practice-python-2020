class RationalNumber:
    def __init__(self, numerator, denominator):
        if type(numerator) != int or type(denominator) != int:
            raise TypeError
        if denominator == 0:
            raise ZeroDivisionError
        self._num = numerator
        self._den = denominator

    def __eq__(self, other):
        return self._den == other._den and self._num == other._num
