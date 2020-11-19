import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_can_create_1_7_fraction_from_str(self):
        frac = Fraction.from_string('1/7')
        self.assertTrue(frac.is_equal(1, 7))


class TestFractionOperations(unittest.TestCase):
    def test_sum_fraction_1_2_1_3(self):
        frac_1 = Fraction(1, 1)
        frac_2 = Fraction(2, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(2, 1))
