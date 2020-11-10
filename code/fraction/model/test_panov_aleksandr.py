import unittest

from fraction.model.fraction import Fraction, InvalidFractionError


class TestFractionClass(unittest.TestCase):
    def test_can_fraction_crete(self):
        frac = Fraction(-1, 2)
        self.assertTrue(frac.is_equal(-1, 2))

    def test_can_add_fraction_to_decimal(self):
        frac = Fraction(1, 2)
        result = Fraction.from_decimal(0.5) + frac
        self.assertTrue(result.is_equal(1, 1))

    def test_cannot_create_null_fraction(self):
        with self.assertRaises(InvalidFractionError):
            Fraction(0, 0)
