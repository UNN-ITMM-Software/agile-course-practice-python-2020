import unittest

from fraction.model.fraction import Fraction, InvalidFractionError


class TestFractionClass(unittest.TestCase):
    def test_incorrect_fraction_is_3_0(self):
        self.assertRaises(InvalidFractionError, Fraction, 3, 0)

    def test_can_create_1_2_fraction(self):
        frac = Fraction(34, 43)
        self.assertTrue(frac.is_equal(34, 43))
