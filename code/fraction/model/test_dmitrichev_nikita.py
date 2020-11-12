import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_equal_neg_fracs_are_equal(self):
        frac = Fraction(6, -5)
        self.assertTrue(frac.is_equal(-6, 5))

    def test_pos_minus_neg(self):
        frac1 = Fraction(7, 6)
        frac2 = Fraction(-1, 1)
        res = frac1 - frac2
        self.assertTrue(res.is_equal(13, 6))
