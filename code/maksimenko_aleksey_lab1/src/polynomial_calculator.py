from itertools import zip_longest
import unittest


def check_zero(coeffs):
        if not isinstance(coeffs, (list, tuple)):
            raise TypeError()
        i = 0
        while coeffs[i] == 0:
            if i == len(coeffs) - 1:
                break
            i += 1
        return coeffs[i:]


class Polynomial:
    def __init__(self, params):
        if not isinstance(params, (list, tuple, Polynomial)):
            raise TypeError()
        if isinstance(params, Polynomial):
            self.coeffs = params.coeffs.copy()
        else:
            if len(params) == 0:
                raise AttributeError()
            if not all(isinstance(coef, int) for coef in params):
                raise TypeError()
            params = check_zero(params)
            if isinstance(params, tuple):
                self.coeffs = list(params)
            else:
                self.coeffs = params

    def __str__(self):
        string = ""
        add_str = " + "
        for n in range(len(self.coeffs)):
            n_coeff = str(self.coeffs[n])
            if (n_coeff == "1") and n != len(self.coeffs)-1:
                    n_coeff = ""
            if n < len(self.coeffs) - 2:
                string = string + n_coeff + "x^" + str(len(self.coeffs) - n - 1) + add_str
            elif n < len(self.coeffs) - 1:
                string = string + n_coeff + "x" + add_str
            else:
                string = string + n_coeff
        return string

    def __repr__(self):
        _str = "Polynomial(" + str(self.coeffs) + ")"
        return _str

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            raise TypeError()
        else:
            if other.coeffs != self.coeffs:
                return False
        return True

    def __add__(self, other):
        res = Polynomial(self.coeffs)
        if isinstance(other, int):
            res.coeffs[-1] += other
            return res
        elif isinstance(other, Polynomial):
            c1 = self.coeffs[::-1]
            c2 = other.coeffs[::-1]
            res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
            res = reversed(res)
            res = list(res)
            res = check_zero(res)
            return Polynomial(res)
        else:
            raise TypeError()

    def __radd__(self, other):
        res = Polynomial(self.coeffs)
        if isinstance(other, int):
            res.coeffs[-1] += other
        else:
            raise TypeError()
        res.coeffs = check_zero(res.coeffs)
        return res

    def __sub__(self, other):
        res = Polynomial(self.coeffs)
        if isinstance(other, int):
            res.coeffs[-1] -= other
            return res
        elif isinstance(other, Polynomial):
            c1 = self.coeffs[::-1]
            c2 = other.coeffs[::-1]
            res = [t1-t2 for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
            res = reversed(res)
            res = list(res)
            res = check_zero(res)
            return Polynomial(res)
        else:
            raise TypeError()

    def __rsub__(self, other):
        res = Polynomial(self.coeffs)
        if isinstance(other, int):
            coeff = [(-1)*t for t in res.coeffs]
            res.coeffs = coeff
            res.coeffs[-1] += other
        else:
            raise TypeError()
        res.coeffs = check_zero(res.coeffs)
        return res

    def __mul__(self, val):
        if isinstance(val, int):
            res = [val*t for t in self.coeffs]
        elif isinstance(val, self.__class__):
            _s = self.coeffs
            _v = val.coeffs
            res = [0]*(len(_s)+len(_v)-1)
            for selfpow, selfco in enumerate(_s):
                for valpow, valco in enumerate(_v):
                    res[selfpow+valpow] += selfco*valco
        else:
            raise TypeError()
        res = list(res)
        res = check_zero(res)
        return self.__class__(res)

    def __rmul__(self, val):
        if isinstance(val, int):
            res = [val*t for t in self.coeffs]
        else:
            raise TypeError()
        res = list(res)
        res = check_zero(res)
        return self.__class__(res)


class TestPolynomial(unittest.TestCase):

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

    def test_sub_poly_and_poly_with_check_zero(self):
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

if __name__ == '__main__':
    unittest.main()
