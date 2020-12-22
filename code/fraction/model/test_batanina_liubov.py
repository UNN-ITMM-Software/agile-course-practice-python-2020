import unittest

from fraction.model.fraction import Fraction, InvalidFractionError


class TestFractionClass(unittest.TestCase):
    def test_can_create_fraction(self):
        frac = Fraction()
        self.assertTrue(isinstance(frac, Fraction))

    def test_cannot_create_x_0_fraction(self):
        with self.assertRaises(InvalidFractionError):
            Fraction(1, 0)

    def test_can_print_fraction(self):
        frac = Fraction(2, 3)
        self.assertEqual('2/3', str(frac))

    def test_none_when_get_nominator_denominator_invalid(self):
        result = Fraction.get_nominator_denominator('a')
        self.assertIsNone(result)

    def test_is_not_fraction_abc(self):
        result = Fraction.is_fraction('abc')
        self.assertFalse(result)


class TestFractionConvertation(unittest.TestCase):
    def test_can_convert_to_decimal_2_5(self):
        frac = Fraction(2, 5)
        self.assertEqual(frac.to_decimal(), 0.4)

    def test_can_convert_from_decimal_minus_1_7(self):
        frac = Fraction.from_decimal(-1.7)
        self.assertTrue(frac.is_equal(-17, 10))


class TestFractionOperations(unittest.TestCase):
    def test_multiply_one_negative_fraction(self):
        frac_1 = Fraction(1, 4)
        frac_2 = Fraction(-2, 7)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(-1, 14))

    def test_multiply_one_negative_fraction_minus_in_denominator(self):
        frac_1 = Fraction(1, 4)
        frac_2 = Fraction(2, -7)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(-1, 14))
