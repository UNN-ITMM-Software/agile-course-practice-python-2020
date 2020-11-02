import unittest
import Fraction

class TestFractionClass(unittest.TestCase):
    def test_default_fraction_is_5_7(self):
        frac = Fraction()
        self.assertTrue(frac.is_equal(5, 7))

class TestFractionOperations(unittest.TestCase):
    def test_multiply_fractions_by_one(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(2, 2)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(1, 2))