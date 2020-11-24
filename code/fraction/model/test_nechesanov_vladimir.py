import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_can_create_fraction_isinstance(self):
        fraction = Fraction()
        self.assertTrue(isinstance(fraction, Fraction))

    def test_can_return_integer(self):
        fraction = Fraction(19, 5)
        self.assertTrue(fraction.get_integer_part() == 3)

    def test_can_return_decimal(self):
        fraction = Fraction(19, 5)
        self.assertTrue(fraction.to_decimal() == 3.8)

    def test_can_create_5_7_fraction_from_str(self):
        frac = Fraction.from_string('5/7')
        self.assertTrue(frac.is_equal(5, 7))
