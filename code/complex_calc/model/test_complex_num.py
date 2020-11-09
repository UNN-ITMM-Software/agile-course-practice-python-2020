import unittest

from complex_calc.model.complex_num import ComplexNum


class TestComplexNumClass(unittest.TestCase):
    def test_can_create_zero_complex_num(self):
        number = ComplexNum()
        self.assertTrue(isinstance(number, ComplexNum))

    def test_can_create_imaginary_num(self):
        number = ComplexNum(im=1)
        self.assertTrue(number.re == 0 and number.im == 1)

    def test_can_create_real_num(self):
        number = ComplexNum(1)
        self.assertTrue(number.re == 1 and number.im == 0)

    def test_can_create_complex_num(self):
        number = ComplexNum(12, 0.23)
        self.assertTrue(number.re == 12 and number.im == 0.23)

    def test_can_print_complex_number(self):
        number = ComplexNum(12, 0.23)
        self.assertEqual('12 + 0.23i', str(number))


class TestComplexNumOperations(unittest.TestCase):
    def test_equal_complex_numbers(self):
        number1 = ComplexNum(1, 2)
        number2 = ComplexNum(1, 2)
        self.assertTrue(number1 == number2)

    def test_equal_complex_number_with_float(self):
        number1 = ComplexNum(3.3, 0)
        self.assertTrue(number1 == 3.3)

    def test_equal_complex_number_with_int(self):
        number1 = ComplexNum(2, 0)
        self.assertTrue(number1 == 2)

    def test_not_equal_complex_numbers(self):
        number1 = ComplexNum(1, 2)
        number2 = ComplexNum(3, 4)
        self.assertTrue(number1 != number2)

    def test_not_equal_complex_number_with_float(self):
        number1 = ComplexNum(1, 2)
        self.assertTrue(number1 != 0.33)

    def test_not_equal_complex_number_with_int(self):
        number1 = ComplexNum(1, 2)
        self.assertTrue(number1 != 3)

    def test_not_equal_im_complex_numbers(self):
        number1 = ComplexNum(1, 2)
        number2 = ComplexNum(1, 4)
        self.assertTrue(number1 != number2)

    def test_not_equal_re_complex_numbers(self):
        number1 = ComplexNum(1, 2)
        number2 = ComplexNum(3, 2)
        self.assertTrue(number1 != number2)

    def test_multiply_complex_numbers(self):
        number1 = ComplexNum(1, 2)
        number2 = ComplexNum(3, 4)
        self.assertEqual(number1*number2, ComplexNum(-5, 10))

    def test_multiply_complex_number_by_float(self):
        number1 = ComplexNum(1, 2)
        self.assertEqual(number1*0.3, ComplexNum(0.3, 0.6))

    def test_multiply_complex_number_by_int(self):
        number1 = ComplexNum(1, 2)
        self.assertEqual(number1*7, ComplexNum(7, 14))

    def test_divide_complex_numbers(self):
        number1 = ComplexNum(1, 2)
        number2 = ComplexNum(3, 4)
        self.assertEqual(number1/number2, ComplexNum(0.44, 0.08))

    def test_divide_complex_number_by_float(self):
        number = ComplexNum(1, 2)
        self.assertEqual(number / 0.1, ComplexNum(10, 20))

    def test_divide_complex_number_by_int(self):
        number = ComplexNum(1, 2)
        self.assertEqual(number / 2, ComplexNum(0.5, 1))

    def test_divide_float_by_complex_number(self):
        number = ComplexNum(3, 4)
        self.assertEqual(0.25 / number, ComplexNum(0.03, -0.04))

    def test_divide_int_by_complex_number(self):
        number = ComplexNum(3, 4)
        self.assertEqual(25 / number, ComplexNum(3, -4))

    def test_add_complex_numbers(self):
        number1 = ComplexNum(1, 2)
        number2 = ComplexNum(3, 4)
        self.assertEqual(number1 + number2, ComplexNum(4, 6))

    def test_add_complex_number_and_float(self):
        number = ComplexNum(1, 2)
        self.assertEqual(number + 0.3, ComplexNum(1.3, 2))

    def test_add_complex_number_and_int(self):
        number = ComplexNum(1, 2)
        self.assertEqual(number + 4, ComplexNum(5, 2))

    def test_sub_complex_numbers(self):
        number1 = ComplexNum(1, 2)
        number2 = ComplexNum(3, 4)
        self.assertEqual(number1-number2, ComplexNum(-2, -2))

    def test_sub_complex_number_and_float(self):
        number1 = ComplexNum(1, 2)
        self.assertTrue((number1 - 0.7).eq_with_precision(ComplexNum(0.3, 2)))

    def test_sub_complex_number_and_int(self):
        number1 = ComplexNum(1, 2)
        self.assertEqual(number1-1, ComplexNum(0, 2))

    def test_sub_float_and_complex_number(self):
        number1 = ComplexNum(1, 2)
        self.assertTrue((0.7 - number1).eq_with_precision(ComplexNum(-0.3, -2)))

    def test_sub_int_and_complex_number(self):
        number1 = ComplexNum(1, 2)
        self.assertEqual(1 - number1, ComplexNum(0, -2))

    def test_negative_complex_number(self):
        number1 = ComplexNum(1, 2)
        self.assertEqual(-number1, ComplexNum(-1, -2))

    def test_conjugate_complex_numbers(self):
        number = ComplexNum(1, 2)
        self.assertEqual(number.conjugate(), ComplexNum(1, -2))

    def test_abs_complex_numbers(self):
        number = ComplexNum(3, 4)
        self.assertEqual(abs(number), 5)


class TestComplicatedComplexNumOperations(unittest.TestCase):
    def test_complicated_complex_number_operations1(self):
        number1 = ComplexNum(3, 4)
        number2 = ComplexNum(1, 2)
        number3 = ComplexNum(3.02, 7.4)
        number4 = ComplexNum(3.88, 4.2)
        self.assertTrue(
            ((abs(number1) + number2/number1)*number3 - number4).eq_with_precision(
                ComplexNum(11.9568, 36.2976)))

    def test_complicated_complex_number_operations2(self):
        number1 = ComplexNum(3, 4)
        number2 = ComplexNum(1, 2)
        number3 = ComplexNum(3.02, 7.4)
        self.assertTrue(
            (abs(number1)*number2*number3 - number3/number1).eq_with_precision(
                ComplexNum(-60.4464, 66.7952)))
