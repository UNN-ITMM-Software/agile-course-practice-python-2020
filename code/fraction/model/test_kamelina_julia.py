import unittest

from fraction.model.fraction import Fraction


class TestFractionOperations(unittest.TestCase):
    def test_sum_pos_fractions(self):
        frac1 = Fraction(1, 3)
        frac2 = Fraction(1, 3)
        res = frac1 + frac2
        self.assertTrue(res.is_equal(2, 3))

    def test_sum_neg_fractions(self):
        frac1 = Fraction(1, 3)
        frac2 = Fraction(-1, 3)
        res = frac1 + frac2
        self.assertTrue(res.is_equal(0, 1))

    def test_sub_pos_fractions(self):
        frac1 = Fraction(1, 3)
        frac2 = Fraction(1, 3)
        res = frac1 - frac2
        self.assertTrue(res.is_equal(0, 1))

    def test_neg_pos_fractions(self):
        frac1 = Fraction(1, 3)
        frac2 = Fraction(-1, 3)
        res = frac1 - frac2
        self.assertTrue(res.is_equal(2, 3))
