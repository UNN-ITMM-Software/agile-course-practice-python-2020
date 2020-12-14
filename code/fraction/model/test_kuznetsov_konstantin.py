import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_invalid_fraction(self):
        self.assertFalse(Fraction.is_fraction('a/b'))

    def test_fraction_reduction(self):
        fraction = Fraction(3, 9)
        self.assertTrue(fraction.is_equal(1, 3))
