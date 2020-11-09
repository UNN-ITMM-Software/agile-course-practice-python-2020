import unittest

from fraction.model.fraction import Fraction, InvalidFractionError


class TwoSimpleTestFraction(unittest.TestCase):
    def test_its(self):
        with self.assertRaises(InvalidFractionError):
            Fraction(0, 0)

    def test_useless(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(3, 2)
        result = frac1 + frac2
        self.assertTrue(result.is_equal(2, 1))

