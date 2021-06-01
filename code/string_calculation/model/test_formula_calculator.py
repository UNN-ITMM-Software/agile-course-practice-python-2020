import unittest

from model.formula_calculator import Calculator


class TestFormulaCalculator(unittest.TestCase):
    def test_create_calculator(self):
        calculator = Calculator()
        self.assertTrue(isinstance(calculator, Calculator))

    def test_integer_number(self):
        calculator = Calculator()
        calculator.set_formula('3')
        expected = 3.0
        self.assertEqual(expected, calculator.eval())

    def test_adding_integer_numbers(self):
        calculator = Calculator()
        calculator.set_formula('1+1')
        expected = 2.0
        self.assertEqual(expected, calculator.eval())

    def test_dividing_integer_numbers(self):
        calculator = Calculator()
        calculator.set_formula('72 / 6')
        expected = 12.0
        self.assertEqual(expected, calculator.eval())

    def test_multiplying_two_integer_numbers(self):
        calculator = Calculator()
        calculator.set_formula('2*2')
        expected = 4.0
        self.assertEqual(expected, calculator.eval())

    def test_multiplying_three_integer_numbers(self):
        calculator = Calculator()
        calculator.set_formula('2*2*2')
        expected = 8.0
        self.assertEqual(expected, calculator.eval())

    def test_multiply_first_calculation_integer_numbers(self):
        calculator = Calculator()
        calculator.set_formula('2*2-2')
        expected = 2.0
        self.assertEqual(expected, calculator.eval())

    def test_order_multiply_first_calculation_integer_numbers(self):
        calculator = Calculator()
        calculator.set_formula('2-2*2')
        expected = -2.0
        self.assertEqual(expected, calculator.eval())

    def test_brackets_calculation_integer_numbers(self):
        calculator = Calculator()
        calculator.set_formula('(2-3)*2')
        expected = -2.0
        self.assertEqual(expected, calculator.eval())

    def test_brackets_calculation_integer_numbers_float_result(self):
        calculator = Calculator()
        calculator.set_formula('(2-3*2)/10')
        expected = -0.4
        self.assertEqual(expected, calculator.eval())

    def test_integer_subtracting(self):
        calculator = Calculator()
        calculator.set_formula('100-10')
        expected = 90.0
        self.assertEqual(expected, calculator.eval())

    def test_brackets_calculation_float_numbers(self):
        calculator = Calculator()
        calculator.set_formula('(2.5-3.5*2.5)/10')
        expected = -0.625
        self.assertEqual(expected, calculator.eval())

    def test_float_subtracting(self):
        calculator = Calculator()
        calculator.set_formula('100.97-10.22')
        expected = 90.75
        self.assertEqual(expected, calculator.eval())

    def test_multiplying_two_float_numbers(self):
        calculator = Calculator()
        calculator.set_formula('2.5*2.5')
        expected = 6.25
        self.assertEqual(expected, calculator.eval())

    def test_float_number(self):
        calculator = Calculator()
        calculator.set_formula('3.12')
        expected = 3.12
        self.assertEqual(expected, calculator.eval())

    def test_adding_float_numbers(self):
        calculator = Calculator()
        calculator.set_formula('1.5+1.9')
        expected = 3.4
        self.assertEqual(expected, calculator.eval())

    def test_dividing_float_numbers(self):
        calculator = Calculator()
        calculator.set_formula('0.625 / 0.25')
        expected = 2.5
        self.assertEqual(expected, calculator.eval())
