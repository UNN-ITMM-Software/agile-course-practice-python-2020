import unittest

from fraction.model.fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_div_fraction(self):
        f1 = Fraction(1, 2)
        self.assertTrue((f1 / f1).is_equal(1, 1))

    def test_mul_fraction(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(0, 3)
        self.assertTrue((f1 * f2).is_equal(0, 1))
