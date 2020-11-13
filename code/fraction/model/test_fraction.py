import unittest

from fraction.model.fraction import Fraction, InvalidFractionError


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

    def test_can_create_1_2_fraction_from_str(self):
        frac = Fraction.from_string('1/2')
        self.assertTrue(frac.is_equal(1, 2))

    def test_can_create_minus_1_2_fraction_from_str(self):
        frac = Fraction.from_string('-1/2')
        self.assertTrue(frac.is_equal(-1, 2))

    def test_can_create_1_fraction_from_str(self):
        frac = Fraction.from_string('1')
        self.assertTrue(frac.is_equal(1, 1))

    def test_cannot_create_x_0_fraction(self):
        with self.assertRaises(InvalidFractionError):
            Fraction(2, 0)

    def test_auto_reduce_fraction(self):
        frac = Fraction(2, 4)
        self.assertTrue(frac.is_equal(1, 2))

    def test_can_print_fraction(self):
        frac = Fraction(5, 7)
        self.assertEqual('5/7', str(frac))

    def test_can_get_int_part(self):
        frac = Fraction(7, 3)
        self.assertEqual(frac.get_integer_part(), 2)

    def test_is_equal_can_return_false_nominator_differs(self):
        frac = Fraction(1, 2)
        self.assertFalse(frac.is_equal(1, 6))

    def test_is_equal_can_return_false_denominator_differs(self):
        frac = Fraction(1, 2)
        self.assertFalse(frac.is_equal(2, 2))

    def test_can_get_nominator_denominator_1_2(self):
        p, q = Fraction.get_nominator_denominator('1/2')
        result = p == '1' and q == '2'
        self.assertTrue(result)

    def test_can_get_nominator_denominator_minus_1_2(self):
        p, q = Fraction.get_nominator_denominator('-1/2')
        result = p == '-1' and q == '2'
        self.assertTrue(result)

    def test_none_when_get_nominator_denominator_invalid(self):
        result = Fraction.get_nominator_denominator('a')
        self.assertIsNone(result)

    def test_is_fraction_1_2(self):
        result = Fraction.is_fraction('1/2')
        self.assertTrue(result)

    def test_is_fraction_minus_1_2(self):
        result = Fraction.is_fraction('-1/2')
        self.assertTrue(result)

    def test_is_fraction_1(self):
        result = Fraction.is_fraction('1')
        self.assertTrue(result)

    def test_is_not_fraction_a(self):
        result = Fraction.is_fraction('a')
        self.assertFalse(result)

    def test_is_not_fraction_empty(self):
        result = Fraction.is_fraction('')
        self.assertFalse(result)


class TestFractionConvertation(unittest.TestCase):
    def test_can_convert_to_decimal_1_2(self):
        frac = Fraction(1, 2)
        self.assertEqual(frac.to_decimal(), 0.5)

    def test_can_convert_from_decimal_0_5(self):
        frac = Fraction.from_decimal(0.5)
        self.assertTrue(frac.is_equal(1, 2))

    def test_can_convert_from_decimal_minus_0_5(self):
        frac = Fraction.from_decimal(-0.5)
        self.assertTrue(frac.is_equal(-1, 2))

    def test_can_convert_from_decimal_0_75(self):
        frac = Fraction.from_decimal(0.75)
        self.assertTrue(frac.is_equal(3, 4))

    def test_can_convert_from_decimal_2_4(self):
        frac = Fraction.from_decimal(2.4)
        self.assertTrue(frac.is_equal(12, 5))

    def test_can_convert_from_decimal_int_1(self):
        frac = Fraction.from_decimal(1)
        self.assertTrue(frac.is_equal(1, 1))

    def test_can_convert_from_decimal_minus_2_4(self):
        frac = Fraction.from_decimal(-2.4)
        self.assertTrue(frac.is_equal(-12, 5))

    def test_can_convert_from_decimal_0_333333333333(self):
        frac = Fraction.from_decimal(0.333333333333)
        self.assertTrue(frac.is_equal(333333333333, 1000000000000))

    def test_can_convert_to_continuous_1071_462(self):
        frac = Fraction(1071, 462)
        expected_coefficients = [2, 3, 7]

        for actual, expected in zip(frac.to_continuous(), expected_coefficients):
            self.assertEqual(actual, expected)

    def test_can_convert_to_continuous_9_4(self):
        frac = Fraction(9, 4)
        expected_coefficients = [2, 4]
        for actual, expected in zip(frac.to_continuous(),
                                    expected_coefficients):
            self.assertEqual(actual, expected)


class TestFractionOperations(unittest.TestCase):
    def test_multiply_fraction(self):
        frac_1 = Fraction(1, 3)
        frac_2 = Fraction(2, 5)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(2, 15))

    def test_multiply_one_negative_fraction(self):
        frac_1 = Fraction(1, 3)
        frac_2 = Fraction(-2, 5)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(-2, 15))

    def test_multiply_one_negative_fraction_minus_in_denominator(self):
        frac_1 = Fraction(1, 3)
        frac_2 = Fraction(2, -5)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(-2, 15))

    def test_multiply_two_negative_fractions(self):
        frac_1 = Fraction(-1, 3)
        frac_2 = Fraction(2, -5)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(2, 15))

    def test_sum_fraction_1_2_1_2(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(1, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(1, 1))

    def test_multiply_fraction_and_int_number(self):
        fraction = Fraction(-1, 6)
        number = 2
        result = number * fraction
        self.assertTrue(result.is_equal(-1, 3))

    def test_multiply_fraction_and_decimal_number(self):
        fraction = Fraction(1, 6)
        number = 2.5
        result = number * fraction
        self.assertTrue(result.is_equal(5, 12))

    def test_multiply_fractions_by_zero(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(0, 2)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(0, 1))

    def test_cannot_divide_fractions_by_zero(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(0, 2)
        with self.assertRaises(InvalidFractionError):
            frac_1 / frac_2

    def test_divide_two_fractions(self):
        frac_1 = Fraction(2, 3)
        frac_2 = Fraction(2, 3)
        result = frac_1 / frac_2
        self.assertTrue(result.is_equal(1, 1))

    def test_substract_fraction_1_2_1_2(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(1, 2)
        result = frac_1 - frac_2
        self.assertTrue(result.is_equal(0, 1))

    def test_sum_fraction_1_2_minus_1_2(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(-1, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(0, 1))

    def test_sum_negative_fraction_minus_1_2_minus_1_2(self):
        frac_1 = Fraction(1, -2)
        frac_2 = Fraction(-1, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(-1, 1))

    def test_sum_fraction_1_2_1_3(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(1, 3)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(5, 6))

    def test_divide_fraction_3_4_3_4(self):
        frac_1 = Fraction(3, 4)
        frac_2 = Fraction(3, 4)
        result = frac_1 / frac_2
        self.assertTrue(result.is_equal(1, 1))

    def test_sum_negative_fraction_0_2_minus_1_3(self):
        frac_1 = Fraction(0, 2)
        frac_2 = Fraction(-1, 3)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(-1, 3))

    def test_sum_fraction_1_1_5_6(self):
        frac_1 = Fraction(1, 1)
        frac_2 = Fraction(5, 6)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(11, 6))

    def test_multiply_fraction_5_6_6_5(self):
        frac_1 = Fraction(5, 6)
        frac_2 = Fraction(6, 5)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(1, 1))
