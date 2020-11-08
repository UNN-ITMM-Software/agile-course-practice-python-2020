import unittest

from gerasimov_dmitry_lab1 import solving_quadratic_equation

sqe = solving_quadratic_equation.solving_quadratic_equation
NO_SOLUTION = solving_quadratic_equation.NO_SOLUTION


class TestSolvingQuadraticEquation(unittest.TestCase):
    def test_all_zero_values(self):
        self.assertRaises(ValueError, sqe, 0, 0, 0)

    def test_values(self):
        self.assertEqual(sqe(1, 0, 0), 0)
        self.assertEqual(sqe(2, 0, 0), 0)
        self.assertEqual(sqe(-3, 0, 0), 0)
        self.assertEqual(sqe(1, 2, 3), NO_SOLUTION)
        self.assertEqual(sqe(-1, 2, -3), NO_SOLUTION)
        self.assertEqual(sqe(7, 4, 3), NO_SOLUTION)
        self.assertEqual(sqe(1, 5, 0), (-5, 0))
        self.assertEqual(sqe(1, -5, 0), (0, 5))
        self.assertEqual(sqe(2, 4, 2), -1)
        self.assertEqual(sqe(8, 8, 2), -0.5)

    def test_float_values(self):
        self.assertEqual(sqe(7, 4, -3), (-1, 0.42857142857142855))
        self.assertEqual(sqe(-10.4, 4.5, -3.4), NO_SOLUTION)
        self.assertEqual(sqe(10.4, 4.5, -3.4), (-0.8276797249896831, 0.3949874172973754))
        self.assertEqual(sqe(-0.5, 3, 1.5), (-0.4641016151377544, 6.464101615137754))

    def test_second_arg_value(self):
        self.assertEqual(sqe(1, 0, 100), NO_SOLUTION)
        self.assertEqual(sqe(-101, 0, -100), NO_SOLUTION)

    def test_correct_input_data_type(self):
        self.assertRaises(TypeError, sqe, 1)
        self.assertRaises(TypeError, sqe, 1, 2)
        self.assertRaises(TypeError, sqe, [1, 2, 3])
        self.assertRaises(TypeError, sqe, 1, 2, 3, 4)
        self.assertRaises(TypeError, sqe, "1", 2, 3)
        self.assertRaises(TypeError, sqe, "1", "2", "3")
        self.assertRaises(TypeError, sqe, "a", "+", "3")
