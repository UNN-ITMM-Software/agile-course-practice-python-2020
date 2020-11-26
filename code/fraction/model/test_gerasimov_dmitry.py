import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_can_create_fraction(self):
        frac = Fraction()
        self.assertTrue(isinstance(frac, Fraction))

    def test_default_fraction_is_0_1(self):
        frac = Fraction()
        self.assertTrue(frac.is_equal(0, 1))

    def test_can_create_1_3_fraction(self):
        frac = Fraction(1, 3)
        self.assertTrue(frac.is_equal(1, 3))


class TestFractionConvert(unittest.TestCase):
    def test_can_convert_from_decimal_0_5(self):
        frac = Fraction.from_decimal(0.25)
        self.assertTrue(frac.is_equal(1, 4))
