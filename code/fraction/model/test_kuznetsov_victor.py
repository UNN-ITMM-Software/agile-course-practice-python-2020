import unittest

from fraction.model.fraction import Fraction


class TestFractionL0(unittest.TestCase):
    def test_fraction_crete(self):
        frac = Fraction(1, 4)
        self.assertTrue(frac.is_equal(1, 4))

    def test_multiply_negative_fraction(self):
        frac_1 = Fraction(-1, 6)
        frac_2 = Fraction(-2, 6)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(1, 18))

    def test_multiply_positive_fraction(self):
        frac_1 = Fraction(1, 6)
        frac_2 = Fraction(2, 6)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(1, 18))
