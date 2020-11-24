import unittest

from fraction.model.fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_add_zero_fraction(self):
        frac_1 = Fraction(0, 1)
        frac_2 = Fraction(1, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(1, 2))

    def test_truediv_of_reverse_fractions(self):
        frac_1 = Fraction(1, 3)
        frac_2 = Fraction(2, 6)
        result = frac_1 / frac_2
        self.assertTrue(result.is_equal(1, 1))
