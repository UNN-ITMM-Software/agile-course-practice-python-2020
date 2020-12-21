import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_is_equal(self):
        frac = Fraction(13, 22)
        self.assertTrue(frac.is_equal(13, 22))

    def test_fraction_sum(self):
        frac_1 = Fraction(-1, 2)
        frac_2 = Fraction(1, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(0, 1))
