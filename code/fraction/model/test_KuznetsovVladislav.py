import unittest

from fraction.model.fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_sum_fraction(self):
        test_fraction_1 = Fraction(9, 11)
        test_fraction_2 = Fraction(1, 11)
        sum_fraction = test_fraction_1 + test_fraction_2
        self.assertTrue(sum_fraction.is_equal(10, 11))

    def test_multiply_fraction(self):
        test_fraction_1 = Fraction(-3, 5)
        test_fraction_2 = Fraction(2, 5)
        mult_fraction = test_fraction_1 * test_fraction_2
        self.assertTrue(mult_fraction.is_equal(-6, 25))
