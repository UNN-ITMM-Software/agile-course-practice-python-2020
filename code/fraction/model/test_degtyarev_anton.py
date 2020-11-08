import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_can_create_fraction(self):
        frac = Fraction()
        self.assertTrue(isinstance(frac, Fraction))

    def test_default_fraction_is_0_1(self):
        frac = Fraction()
        self.assertTrue(frac.is_equal(0, 1))

    def test_can_create_1_5_fraction(self):
        frac = Fraction(1, 5)
        self.assertTrue(frac.is_equal(1, 5))

    def test_is_not_fraction_abc(self):
        result = Fraction.is_fraction('abc')
        self.assertFalse(result)