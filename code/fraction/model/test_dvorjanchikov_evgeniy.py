import unittest

from fraction.model.fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_multiply_zero_fraction(self):
        frac_1 = Fraction(0, 1)
        frac_2 = Fraction(1, 2)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(0, 1))

    def test_multyply_reverse_fraction(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(2, 1)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(1, 1))
