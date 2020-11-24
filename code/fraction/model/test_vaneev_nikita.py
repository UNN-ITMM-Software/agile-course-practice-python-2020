import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):

    def test_can_create_1_4_fraction(self):
        frac = Fraction(1, 4)
        self.assertTrue(frac.is_equal(1, 4))

    def test_can_create_1_5_fraction(self):
        frac = Fraction(1, 5)
        self.assertTrue(frac.is_equal(1, 5))
