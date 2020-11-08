import unittest

from gerasimov_dmitry_lab1 import solving_quadratic_equation

sqe = solving_quadratic_equation.solving_quadratic_equation


class TestSolvingQuadraticEquation(unittest.TestCase):
    def test_all_zero_values(self):
        self.assertRaises(ValueError, sqe, 0, 0, 0)

    def test_values(self):
        self.assertEqual(sqe(1, 0, 0), 0)
        self.assertEqual(sqe(2, 0, 0), 0)
        self.assertEqual(sqe(-3, 0, 0), 0)
