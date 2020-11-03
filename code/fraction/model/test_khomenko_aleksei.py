import unittest

from fraction.model.fraction import Fraction


class TestFractionSimple(unittest.TestCase):

    def test_can_create_5_6_fraction(self):
        frac = Fraction(5, 6)
        self.assertTrue(frac.is_equal(5, 6))

    def test_multiply_two_positive_fractions(self):
        frac_1 = Fraction(5, 6)
        frac_2 = Fraction(5, 7)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(25, 42))
