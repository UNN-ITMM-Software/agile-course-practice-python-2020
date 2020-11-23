import unittest

from fraction.model.fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_divide_two_same_fraction(self):
        frac_1 = Fraction(3, 5)
        frac_2 = Fraction(3, 5)
        result = frac_1 / frac_2
        self.assertEqual(result.p, 1)
        self.assertEqual(result.q, 1)

    def test_multiply_by_1(self):
        frac_1 = Fraction(3, 10)
        frac_2 = Fraction(1, 1)
        result = frac_1 * frac_2
        self.assertEqual(result.p, 3)
        self.assertEqual(result.q, 10)
