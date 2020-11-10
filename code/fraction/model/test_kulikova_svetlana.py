import unittest

from fraction.model.fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_sum(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 3)
        res = frac1 + frac2
        self.assertTrue(res.is_equal(7, 6))

    def test_mul(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 3)
        res = frac1 * frac2
        self.assertTrue(res.is_equal(1, 3))