import unittest
from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_can_create_5_7_fraction(self):
        frac = Fraction(5, 7)
        self.assertTrue(frac.is_equal(5, 7))


class TestFractionOperations(unittest.TestCase):
    def test_multiply_fractions_1_3_3_1(self):
        frac_1 = Fraction(1, 3)
        frac_2 = Fraction(3, 1)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(1, 1))
