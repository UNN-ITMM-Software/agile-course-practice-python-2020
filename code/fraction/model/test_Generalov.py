import unittest

from fraction.model.fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_create_fraction(self):
        frac = Fraction()
        self.assertTrue(isinstance(frac, Fraction))

    def test_multiply_fraction(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(3, 4)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(3, 8))

    def test_sum_fraction_1_2_3_4(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(3, 4)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(5, 4))
