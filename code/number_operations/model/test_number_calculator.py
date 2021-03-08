import unittest

from number_operations.model.number_calculator import Calculator


class TestNumberCalculator(unittest.TestCase):
    def test_create_calculator(self):
        calculator = Calculator()
        self.assertTrue(isinstance(calculator, Calculator))

    def test_adding_decimal_numbers(self):
        calculator = Calculator()
        calculator.set_first('33', 10)
        calculator.set_second('77', 10)
        expected = '110'
        self.assertEqual(expected, calculator.add(10))

    def test_adding_binary_numbers(self):
        calculator = Calculator()
        calculator.set_first('1010', 2)
        calculator.set_second('1111', 2)
        expected = '25'
        self.assertEqual(expected, calculator.add(10))

    def test_dividing_octal_numbers(self):
        calculator = Calculator()
        calculator.set_first('74', 8)
        calculator.set_second('6', 8)
        expected = '12'
        self.assertEqual(expected, calculator.divide(8))

    def test_multiplying_hex_numbers(self):
        calculator = Calculator()
        calculator.set_first('deadbeef', 16)
        calculator.set_second('c0ffee', 16)
        expected = 'a7e0ed49f79332'
        self.assertEqual(expected, calculator.multiply(16))

    def test_subtracting_decimal_and_binary(self):
        calculator = Calculator()
        calculator.set_first('100', 10)
        calculator.set_second('1010', 2)
        expected = '90'
        self.assertEqual(expected, calculator.subtract(10))
