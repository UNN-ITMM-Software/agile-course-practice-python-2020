import unittest

from maksimenko_aleksey_lab1.src.polynomial_calculator import Polynomial, check_zero


class TestPolynomial(unittest.TestCase):

    # CHECK_ZERO TESTS

    def passing_a_string(self):
        with self.assertRaises(TypeError):
            check_zero('a')

    def zeros_at_the_beginning(self):
        self.assertEqual([1, 2, 3], check_zero([0, 1, 2, 3]))

    def zeros_at_the_beginning_and_in_the_middle(self):
        self.assertEqual([1, 0, 3], check_zero([0, 0, 1, 0, 3]))

    def all_zeros(self):
        self.assertEqual([0], check_zero([0, 0, 0]))

    # INIT TESTS

    def test_init_param_list(self):
        _list = list([1, 2, 3])
        self.assertEqual(_list, Polynomial(_list).coeffs)

    def test_init_param_tuple(self):
        _tuple = tuple([1, 2, 3])
        self.assertEqual([1, 2, 3], Polynomial(_tuple).coeffs)

    def test_init_param_polynomial(self):
        pol1 = Polynomial([1, 2, 3])
        pol2 = Polynomial(pol1)
        self.assertEqual(pol1.coeffs, pol2.coeffs)

    def test_init_with_start_zeros_in_param(self):
        self.assertEqual([1, 2, -4], Polynomial((0, 0, 0, 1, 2, -4)).coeffs)

    def test_init_param_zero(self):
        self.assertEqual([0], Polynomial([0]).coeffs)

    def test_init_param_only_zeros(self):
        self.assertEqual([0], Polynomial([0, 0, 0]).coeffs)

    def test_init_fails_on_empty_param(self):
        with self.assertRaises(AttributeError):
            Polynomial([])

    def test_init_fails_on_incorrect_input_param(self):
        with self.assertRaises(TypeError):
            Polynomial(1)

    def test_init_fails_on_incorrect_coeffs_type_string(self):
        with self.assertRaises(TypeError):
            Polynomial(['42453', '24'])

    def test_init_fails_on_incorrect_coeffs_type_float(self):
        with self.assertRaises(TypeError):
            Polynomial([2.0, 6.1])

    # SUM TESTS

    def test_sum_poly_and_number(self):
        self.assertEqual(Polynomial([1, 2, 4]), Polynomial([1, 2, 3]) + 1)

    def test_sum_number_and_poly(self):
        self.assertEqual(Polynomial([1, 2, 4]), 1 + Polynomial([1, 2, 3]))

    def test_sum_poly_and_zero(self):
        self.assertEqual(Polynomial([1, 2, 3]), Polynomial([1, 2, 3]) + 0)

    def test_sum_fail_incorrect_type_and_poly(self):
        with self.assertRaises(TypeError):
            'str' + Polynomial([1, 2, 3])

    def test_sum_poly_and_poly(self):
        self.assertEqual(Polynomial([4, 6, 8, 10]), Polynomial([1, 2, 3]) + Polynomial([4, 5, 6, 7]))

    def test_sum_poly_and_poly_with_check_zero(self):
        self.assertEqual(Polynomial([1, 0]), Polynomial([1, 2, 3]) + Polynomial([-1, -1, -3]))

    # SUB TESTS

    def test_sub_poly_and_number(self):
        self.assertEqual(Polynomial([1, 2, 2]), Polynomial([1, 2, 3]) - 1)

    def test_sub_number_and_poly(self):
        self.assertEqual(Polynomial([-1, -2, -2]), 1 - Polynomial([1, 2, 3]))

    def test_sub_poly_and_zero(self):
        self.assertEqual(Polynomial([1, 2, 3]), Polynomial([1, 2, 3]) - 0)

    def test_sub_fail_incorrect_type_and_poly(self):
        with self.assertRaises(TypeError):
            'str' - Polynomial([1, 2, 3])

    def test_sub_poly_and_poly(self):
        self.assertEqual(Polynomial([-4, -4, -4, -4]), Polynomial([1, 2, 3]) - Polynomial([4, 5, 6, 7]))

    def test_sub_poly_and_poly_with_check_zero(self):
        self.assertEqual(Polynomial([1, 0]), Polynomial([1, 2, 3]) - Polynomial([1, 1, 3]))

    # MUL TESTS

    def test_mul_poly_and_number(self):
        self.assertEqual(Polynomial([2, 4, 6]), Polynomial([1, 2, 3]) * 2)

    def test_mul_number_and_poly(self):
        self.assertEqual(Polynomial([2, 4, 6]), 2 * Polynomial([1, 2, 3]))

    def test_mul_poly_and_zero(self):
        self.assertEqual(Polynomial([0]), Polynomial([1, 2, 3]) * 0)

    def test_mul_fail_incorrect_type_and_poly(self):
        with self.assertRaises(TypeError):
            'str' * Polynomial([1, 2, 3])

    def test_mul_poly_and_poly(self):
        self.assertEqual(Polynomial([4, 13, 28, 34, 32, 21]),
                         Polynomial([1, 2, 3]) * Polynomial([4, 5, 6, 7]))

    def test_mul_poly_and_poly_with_check_zero(self):
        self.assertEqual(Polynomial([1, 0, 1, 0, 0]), Polynomial([1, 0, 1]) * Polynomial([1, 0, 0]))

    # EQUAL TESTS

    def test_eq_poly(self):
        self.assertTrue(Polynomial([1, 2, 3, 4]) == Polynomial([1, 2, 3, 4]))

    def test_eq_poly_with_zero(self):
        self.assertTrue(Polynomial([0, 1, 2, 3, 4]) == Polynomial([1, 2, 3, 4]))

    def test_not_eq_poly(self):
        self.assertFalse(Polynomial([1, 2, 3, 4]) == Polynomial([1, 2, 3, 5]))

    def test_eq_fail_incorrect_type(self):
        with self.assertRaises(TypeError):
            Polynomial([0, 1, 4, 0, -8]) == 'test'

    # REPR TESTS

    def test_repr(self):
        self.assertEqual('Polynomial([1, 2, 3])', repr(Polynomial([1, 2, 3])))

    def test_repr_with_zeros(self):
        self.assertEqual('Polynomial([1, 2, 3])', repr(Polynomial([0, 1, 2, 3])))

    # STR TESTS

    def test_str(self):
        self.assertEqual('x^2 + x + 1',  str(Polynomial([1, 1, 1])))

    def test_str_with_zeros(self):
        self.assertEqual('x^2 + 2x + 3', str(Polynomial([0, 0, 1, 2, 3])))
