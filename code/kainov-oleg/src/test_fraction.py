import unittest

from fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_can_create_fraction(self):
        frac = Fraction()
        self.assertTrue(isinstance(frac, Fraction))

    def test_default_fraction_is_0_1(self):
        frac = Fraction()
        self.assertEqual(frac.p, 0)
        self.assertEqual(frac.q, 1)

    def test_can_create_1_2_fraction(self):
        frac = Fraction(1, 2)
        self.assertEqual(frac.p, 1)
        self.assertEqual(frac.q, 2)
