import unittest

from fraction.model.fraction import Fraction

class TestFractionClass(unittest.TestCase):
    def test_div_sum_equal_sum_div(self):
        frac1 = Fraction(10, 2)
        frac2 = Fraction(-5, 2)
        frac3 = Fraction(7, 2)
        frac = frac1 + frac2 + frac3
        self.assertTrue(frac.is_equal(12, 2))

    def test_mut_sum_equal_sum_mut(self):
        frac1 = Fraction(2, 3)
        frac2 = Fraction(7, 5)
        frac3 = Fraction(5, 2)
        res = (frac1 + frac2) * frac3
        res1 = (frac1 + frac3) * (frac2 + frac3)
        self.assertTrue(res.__eq__(res1))
