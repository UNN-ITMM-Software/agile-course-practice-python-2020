
import unittest

from fraction.model.fraction import Fraction, InvalidFractionError


class TestFractionOperations(unittest.TestCase):
    def test_sum_fraction(self):
        f1 = Fraction(2, 4)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertTrue(result.is_equal(5, 6))

    def test_sub_fraction(self):
        f1 = Fraction(2, 4)
        f2 = Fraction(1, 3)
        result = f1 - f2
        self.assertTrue(result.is_equal(1, 6))

    def test_mul_fraction(self):
        f1 = Fraction(-2, 4)
        f2 = Fraction(-1, 3)
        result = f1 * f2
        self.assertTrue(result.is_equal(1, 6))

    def test_div_fraction_by_zero(self):
        f1 = Fraction(-2, 4)
        f2 = Fraction(0, 3)
        with self.assertRaises(InvalidFractionError):
            f1 / f2
