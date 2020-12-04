import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_can_create_fraction(self):
        fraction = Fraction()
        self.assertTrue(isinstance(fraction, Fraction))

    def test_sum_frations(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(3, 4)
        res = frac_1 + frac_2
        self.assertTrue(res.is_equal(5, 4))

    def test_sub_frations(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(3, 4)
        res = frac_2 - frac_1
        self.assertTrue(res.is_equal(1, 4))

    def test_mul_frations(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(3, 4)
        res = frac_2 * frac_1
        self.assertTrue(res.is_equal(3, 8))
