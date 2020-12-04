import unittest

from fraction.model.fraction import Fraction


class TestFractionAG(unittest.TestCase):

    def test_can_create_1_2_fraction(self):
        frac = Fraction(1, 2)
        self.assertTrue(frac.is_equal(1, 2))

    def test_multiply_fraction(self):
        frac_1 = Fraction(1, 3)
        frac_2 = Fraction(2, 5)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(2, 15))
