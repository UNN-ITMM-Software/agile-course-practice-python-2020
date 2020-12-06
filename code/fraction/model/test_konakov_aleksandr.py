import unittest

from fraction.model.fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_fraction_mul(self):
        f1 = Fraction(1, 3)
        f2 = Fraction(3, 2)
        m = f1 * f2
        self.assertTrue(m.is_equal(1, 2))

    def test_fraction_reduce(self):
        f = Fraction(2, 10)
        self.assertTrue(f.is_equal(1, 5))
