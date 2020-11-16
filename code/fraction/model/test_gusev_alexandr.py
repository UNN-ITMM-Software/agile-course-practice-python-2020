import unittest

from fraction.model.fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_add_zero_fraction(self):
        frac_1 = Fraction(0, 1)
        frac_2 = Fraction(1, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(1, 2))

    def test_can_fraction_create(self):
        frac = Fraction(-1, 2)
        self.assertTrue(frac.is_equal(-1, 2))