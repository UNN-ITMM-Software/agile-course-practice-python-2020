import unittest

from fraction.model.fraction import Fraction, InvalidFractionError


class TestFractionClass(unittest.TestCase):

    def test_init_with_zero_raise(self):
        with self.assertRaises(InvalidFractionError):
            Fraction(1, 0)

    def test_plus(self):
        frac = Fraction(2, 5)
        frac_two = Fraction(1, 5)
        result = frac + frac_two
        self.assertTrue(result.is_equal(3, 5))

    def test_minus(self):
        frac = Fraction(2, 5)
        frac_two = Fraction(1, 5)
        result = frac - frac_two
        self.assertTrue(result.is_equal(1, 5))
