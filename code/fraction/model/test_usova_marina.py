import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_is_fraction_1_2_with_space(self):
        result = Fraction.is_fraction('1 / 2')
        self.assertFalse(result)


class TestFractionOperations(unittest.TestCase):
    def test_substract_fraction_minus_1_2_1_2(self):
        frac_1 = Fraction(-1, 2)
        frac_2 = Fraction(1, 2)
        result = frac_1 - frac_2
        self.assertTrue(result.is_equal(-1, 1))

    def test_substract_fraction_1_2_1_minus_2(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(1, -2)
        result = frac_1 - frac_2
        self.assertTrue(result.is_equal(1, 1))

    def test_substract_negative_fraction(self):
        frac_1 = Fraction(-1, -3)
        frac_2 = Fraction(-1, -2)
        result = frac_1 - frac_2
        self.assertTrue(result.is_equal(-1, 6))
