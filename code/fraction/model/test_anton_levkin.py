import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_can_create_str_from_fraction(self):
        frac = Fraction(p=3, q=4)
        self.assertEqual(str(frac), '3/4')

    def test_mul_fraction(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(0, 3)
        self.assertTrue((f1 * f2).is_equal(0, 1))