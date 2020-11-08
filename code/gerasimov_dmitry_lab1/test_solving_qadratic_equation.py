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
        self.assertEqual(sqe(1, 5, 0), (-5, 0))
        self.assertEqual(sqe(1, -5, 0), (0, 5))

    def test_second_arg_value(self):
        self.assertEqual(sqe(1, 0, 100), NO_SOLUTION)
        self.assertEqual(sqe(-101, 0, -100), NO_SOLUTION)
