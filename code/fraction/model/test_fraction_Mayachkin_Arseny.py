import unittest

from fraction.model.fraction import Fraction, InvalidFractionError


class TestFractionClass(unittest.TestCase):
    def test_raise_init_error(self):
        with self.assertRaises(InvalidFractionError):
            Fraction(5, 0)

    def test_is_equal(self):
        frac = Fraction(1, -3)
        self.assertFalse(frac.is_equal(-1, 3))

    def test_fraction_sum(self):
        frac_1 = Fraction(1, 5)
        frac_2 = Fraction(3, 4)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(19, 20))
