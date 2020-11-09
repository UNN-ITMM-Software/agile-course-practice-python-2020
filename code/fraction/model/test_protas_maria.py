import unittest

from fraction.model.fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_create_fraction(self):
        fraction = Fraction()
        self.assertTrue(isinstance(fraction, Fraction))

    def test_fraction_sum(self):
        frac_1 = Fraction(5, 7)
        frac_2 = Fraction(3, 5)
        res = frac_1 + frac_2
        self.assertTrue(res.is_equal(46, 35))

    def test_sub_fraction(self):
        frac_1 = Fraction(1, 3)
        frac_2 = Fraction(1, 2)
        res = frac_2 - frac_1
        self.assertTrue(res.is_equal(1, 6))

    def test_mul_negative_fraction(self):
        frac_1 = Fraction(-1, 3)
        frac_2 = Fraction(-1, 2)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(1, 6))

    def test_mul_positive_fraction(self):
        frac_1 = Fraction(1, 3)
        frac_2 = Fraction(1, 2)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(1, 6))