import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_is_not_fraction_a(self):
        result = Fraction.is_fraction('1/b')
        self.assertFalse(result)

    def test_that_2_4_is_equal_1_2(self):
        frac = Fraction(2, 4)
        self.assertTrue(frac.is_equal(1, 2))
