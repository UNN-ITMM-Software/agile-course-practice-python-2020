import unittest

from fraction import Fraction, GCD


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

    # def test_auto_reduce_fraction(self):
    #     frac = Fraction(2, 4)
    #     self.assertEqual(frac.p, 1)
    #     self.assertEqual(frac.q, 2)


class TestGCD(unittest.TestCase):
    def test_GCD_1_1(self):
        self.assertEqual(GCD(1, 1), 1)

    def test_GCD_2_4(self):
        self.assertEqual(GCD(2, 4), 2)

    def test_GCD_81_35(self):
        self.assertEqual(GCD(81, 35), 1)
