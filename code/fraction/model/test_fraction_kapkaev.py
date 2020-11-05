import unittest

from fraction.model.fraction import Fraction, InvalidFractionError


class TestFractionOperations(unittest.TestCase):
    def test_multiply_fraction(self):
        frac_1 = Fraction(0, 3)
        frac_2 = Fraction(1, 5)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(0, 1))

    def test_multiply_negative_fraction(self):
        frac_1 = Fraction(-1, 3)
        frac_2 = Fraction(1, 2)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(-1, 6))
