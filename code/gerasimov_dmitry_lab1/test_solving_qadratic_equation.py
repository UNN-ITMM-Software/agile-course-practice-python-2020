import unittest

from gerasimov_dmitry_lab1.solving_quadratic_equation import QuadraticEquation, is_correct_input_type


class TestSolvingQuadraticEquation(unittest.TestCase):
    def test_create_quadratic_equation(self):
        quadratic_equation = QuadraticEquation()
        self.assertTrue(isinstance(quadratic_equation, QuadraticEquation))

    def test_is_set_default_values(self):
        quadratic_equation = QuadraticEquation()
        a = 1
        b = 0
        c = 0
        self.assertEqual(a, quadratic_equation.a)
        self.assertEqual(b, quadratic_equation.b)
        self.assertEqual(c, quadratic_equation.c)

    def test_not_all_values(self):
        a = 5
        b = 4
        quadratic_equation = QuadraticEquation(a)
        self.assertEqual(quadratic_equation.a, a)
        self.assertEquals(quadratic_equation.b, quadratic_equation.c, 0)

        quadratic_equation = QuadraticEquation(a, b)
        self.assertEqual(quadratic_equation.a, a)
        self.assertEqual(quadratic_equation.b, b)
        self.assertEqual(quadratic_equation.c, 0)

    def test_set_value_to_quadratic_equation(self):
        a = 9
        b = 8
        c = 7
        quadratic_equation = QuadraticEquation(a, b, c)
        self.assertEqual(a, quadratic_equation.a)
        self.assertEqual(b, quadratic_equation.b)
        self.assertEqual(c, quadratic_equation.c)

    def test_all_zero_values(self):
        self.assertRaises(ValueError, QuadraticEquation, 0, 0, 0)

    def test_values(self):
        self.assertEqual(QuadraticEquation(1, 0, 0).solution(), [0])
        self.assertEqual(QuadraticEquation(2, 0, 0).solution(), [0])
        self.assertEqual(QuadraticEquation(-3, 0, 0).solution(), [0])
        self.assertEqual(QuadraticEquation(1, 2, 3).solution(), [])
        self.assertEqual(QuadraticEquation(-1, 2, -3).solution(), [])
        self.assertEqual(QuadraticEquation(7, 4, 3).solution(), [])
        self.assertEqual(QuadraticEquation(1, 5, 0).solution(), [-5, 0])
        self.assertEqual(QuadraticEquation(1, -5, 0).solution(), [0, 5])
        self.assertEqual(QuadraticEquation(2, 4, 2).solution(), [-1])
        self.assertEqual(QuadraticEquation(8, 8, 2).solution(), [-0.5])
        self.assertEqual(QuadraticEquation(1, 0, -2).solution(), [-1.4142135623730951, 1.4142135623730951])

    def test_float_values(self):
        self.assertEqual(QuadraticEquation(7, 4, -3).solution(), [-1, 0.42857142857142855])
        self.assertEqual(QuadraticEquation(-10.4, 4.5, -3.4).solution(), [])
        self.assertEqual(
            QuadraticEquation(10.4, 4.5, -3.4).solution(),
            [-0.8276797249896831, 0.3949874172973754])
        self.assertEqual(
            QuadraticEquation(-0.5, 3, 1.5).solution(),
            [-0.4641016151377544, 6.464101615137754])

    def test_second_arg_value(self):
        self.assertEqual(QuadraticEquation(1, 0, 100).solution(), [])
        self.assertEqual(QuadraticEquation(-101, 0, -100).solution(), [])

    def test_check_correct_input_value(self):
        self.assertTrue(is_correct_input_type(0))
        self.assertTrue(is_correct_input_type(1))
        self.assertTrue(is_correct_input_type(-1))
        self.assertTrue(is_correct_input_type(1.5456))
        self.assertTrue(is_correct_input_type(-1.5456))
        self.assertFalse(is_correct_input_type("1"))
        self.assertFalse(is_correct_input_type("1.5"))
        self.assertFalse(is_correct_input_type([1]))
        self.assertFalse(is_correct_input_type([1, 2]))
        self.assertFalse(is_correct_input_type(False))

    def test_correct_input_data_type(self):
        self.assertRaises(TypeError, QuadraticEquation, [1, 2, 3])
        self.assertRaises(TypeError, QuadraticEquation, 1, 2, 3, 4)
        self.assertRaises(TypeError, QuadraticEquation, "1", 2, 3)
        self.assertRaises(TypeError, QuadraticEquation, "1", "2", "3")
        self.assertRaises(TypeError, QuadraticEquation, "a", "+", "3")

    def test_string_output_answer(self):
        self.assertEqual(QuadraticEquation(1, 0, 100).solution_in_string_format(), 'No solution')
        self.assertEqual(QuadraticEquation(1, 0, 0).solution_in_string_format(), 'Answer:\n x = 0.0')
        self.assertEqual(QuadraticEquation(2, 4, 2).solution_in_string_format(), 'Answer:\n x = -1.0')

        self.assertEqual(
            QuadraticEquation(1, 5, 0).solution_in_string_format(),
            'Answers:\n x1 = -5.0,\n x2 = 0.0')
        self.assertEqual(
            QuadraticEquation(7, 4, -3).solution_in_string_format(),
            'Answers:\n x1 = -1.0,\n x2 = 0.42857142857142855')
