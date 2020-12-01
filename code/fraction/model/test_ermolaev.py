import unittest

from fraction.model.fraction import Fraction


class TestFractionOperations(unittest.TestCase):
    def test_multiply_fraction(self):
        frac_1 = Fraction(-1, 2)
        frac_2 = Fraction(1, 2)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(-1, 4))

    def test_sum_fraction(self):
        frac_1 = Fraction(-1, 2)
        frac_2 = Fraction(1, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(0, 1))
