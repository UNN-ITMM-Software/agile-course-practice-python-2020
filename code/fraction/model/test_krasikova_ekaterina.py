import unittest

from fraction.model.fraction import Fraction


class TestFractionOperations(unittest.TestCase):
    def test_multiply_fraction(self):
        frac_1 = Fraction(3, 8)
        frac_2 = Fraction(2, 5)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(3, 20))

    def test_sum_fraction(self):
        frac_1 = Fraction(1, 3)
        frac_2 = Fraction(1, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(5, 6))

    def test_divide_two_fractions(self):
        frac_1 = Fraction(1, 3)
        frac_2 = Fraction(2, 3)
        result = frac_1 / frac_2
        self.assertTrue(result.is_equal(1, 2))

    def test_substract_fraction(self):
        frac_1 = Fraction(1, 5)
        frac_2 = Fraction(1, 5)
        result = frac_1 - frac_2
        self.assertTrue(result.is_equal(0, 1))
