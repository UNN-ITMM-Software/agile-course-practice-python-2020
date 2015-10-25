import unittest

from fraction import Fraction, InvalidFractionError


class TestFractionClass(unittest.TestCase):
    def test_can_create_fraction(self):
        frac = Fraction()
        self.assertTrue(isinstance(frac, Fraction))

    def test_default_fraction_is_0_1(self):
        frac = Fraction()
        self.assertTrue(frac.is_equal(0, 1))

    def test_can_create_1_2_fraction(self):
        frac = Fraction(1, 2)
        self.assertTrue(frac.is_equal(1, 2))

    def test_cannot_create_x_0_fraction(self):
        with self.assertRaises(InvalidFractionError):
            Fraction(2, 0)

    def test_auto_reduce_fraction(self):
        frac = Fraction(2, 4)
        self.assertTrue(frac.is_equal(1, 2))

    def test_multiply_fraction(self):
        frac_1 = Fraction(1, 3)
        frac_2 = Fraction(2, 5)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(2, 15))

    def test_sum_fraction_1_2_1_2(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(1, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(1, 1))

    def test_sum_fraction_1_2_minus_1_2(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(-1, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(0, 1))

    def test_sum_fraction_1_2_1_3(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(1, 3)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(5, 6))

    def test_can_print_fraction(self):
        frac = Fraction(5, 7)
        self.assertEqual(str(frac), '5/7')

    def test_can_convert_to_decimal_1_2(self):
        frac = Fraction(1, 2)
        self.assertEqual(frac.to_decimal(), 0.5)

    def test_can_convert_from_decimal_0_5(self):
        frac = Fraction.from_decimal(0.5)
        self.assertTrue(frac.is_equal(1, 2))

    def test_can_convert_from_decimal_0_75(self):
        frac = Fraction.from_decimal(0.75)
        self.assertTrue(frac.is_equal(3, 4))

    def test_can_convert_from_decimal_0_333333333333(self):
        frac = Fraction.from_decimal(0.333333333333)
        self.assertTrue(frac.is_equal(333333333333, 1000000000000))

    def test_can_get_int_part(self):
        frac = Fraction(7, 3)
        self.assertEqual(frac.get_int_part(), 2)
