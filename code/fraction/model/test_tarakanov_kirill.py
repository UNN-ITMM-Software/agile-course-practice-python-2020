import unittest

from fraction.model.fraction import Fraction


class SimpleOperationsTests(unittest.TestCase):
    def test_sum_fraction(self):
        frac1 = Fraction(4, 7)
        frac2 = Fraction(1, 3)
        sum_result = frac1 + frac2
        self.assertTrue(sum_result.is_equal(19, 21))

    def test_divide_two_fractions(self):
        frac1 = Fraction(4, 7)
        frac2 = Fraction(2, 3)
        divide_result = frac1 / frac2
        self.assertTrue(divide_result.is_equal(6, 7))
