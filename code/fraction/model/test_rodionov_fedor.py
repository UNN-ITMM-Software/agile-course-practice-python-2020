import unittest

from fraction.model.fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_reducing_fraction(self):
        fraction = Fraction(3, 6)
        self.assertTrue(fraction.is_equal(1, 2))

    def test_sum_fraction(self):
        first_fraction = Fraction(3, 5)
        second_fraction = Fraction(1, 3)
        result = first_fraction + second_fraction
        self.assertTrue(result.is_equal(14, 15))