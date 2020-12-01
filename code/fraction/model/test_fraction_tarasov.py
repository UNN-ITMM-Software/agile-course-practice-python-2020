import unittest

from fraction.model.fraction import Fraction


class FractionTestClass(unittest.TestCase):

    def test_fraction_init(self):
        fraction = Fraction(5, 9)
        self.assertTrue(fraction.is_equal(5, 9))

    def test_auto_reducing(self):
        fraction = Fraction(2, 4)
        self.assertTrue(fraction.is_equal(1, 2))
