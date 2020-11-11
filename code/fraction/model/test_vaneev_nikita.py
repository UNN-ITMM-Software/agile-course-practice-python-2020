import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):

    def test_default_fraction_is_4_6(self):
        frac = Fraction()
        self.assertTrue(frac.is_equal(4, 6))

    def test_can_create_7_2_fraction(self):
        frac = Fraction(1, 3)
        self.assertTrue(frac.is_equal(7, 2))
