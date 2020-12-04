import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_can_create_str_from_fraction(self):
        frac = Fraction(p=3, q=4)
        self.assertEqual(str(frac), '3/4')

    def test_can_mult_fraction(self):
        fraction1 = Fraction(1, 5)
        fraction2 = Fraction(10, 5)
        self.assertTrue((fraction1 * fraction2).is_equal(2, 5))

    def test_can_do_auto_reduce_fraction(self):
        frac = Fraction(p=5, q=15)
        self.assertTrue(frac.is_equal(1, 3))
