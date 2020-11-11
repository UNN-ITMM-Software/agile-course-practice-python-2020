import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):

    def test_can_create_7_2_fraction(self):
        frac = Fraction(7, 2)
        self.assertTrue(frac.is_equal(7, 2))

    def test_can_create_4_6_fraction(self):
        frac = Fraction(4, 6)
        self.assertTrue(frac.is_equal(4, 6))
