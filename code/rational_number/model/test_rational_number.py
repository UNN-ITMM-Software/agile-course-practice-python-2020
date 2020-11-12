import unittest

from rational_number.model.rational_number import RationalNumber


class TestRationalNumberClass(unittest.TestCase):
    def test_can_create_rational_number(self):
        number = RationalNumber(-1, 2)
        self.assertTrue(isinstance(number, RationalNumber))

    def test_can_not_create_divide_zero_rational_number(self):
        with self.assertRaises(ZeroDivisionError):
            RationalNumber(1, 0)

    def test_can_not_create_rational_number_from_bad_str(self):
        with self.assertRaises(TypeError):
            RationalNumber('a', 1)
        with self.assertRaises(TypeError):
            RationalNumber(1, 'b')

    def test_can_check_equality_rational_numbers(self):
        number = RationalNumber(-1, 2)
        self.assertEquals(number, RationalNumber(-1, 2))
        self.assertEquals(number, RationalNumber(1, -2))

    def test_reduce_rational_number1(self):
        number = RationalNumber(-1, 2)
        self.assertEquals(number, RationalNumber(2, -4))

    def test_reduce_rational_number2(self):
        number = RationalNumber(-27, 144)
        self.assertEquals(number, RationalNumber(3, -16))

    def test_can_check_not_equality_rational_numbers(self):
        number = RationalNumber(-1, 2)
        self.assertNotEquals(number, RationalNumber(1, 2))
        self.assertNotEquals(number, RationalNumber(-1, 3))
