import unittest

from numerical_integration.model.numerical_integration import NumericalIntegrator


class TestNumericalIntegratorClass(unittest.TestCase):

    def test_numerical_integratior_can_create(self):
        numerical_integratior = NumericalIntegrator()
        self.assertTrue(isinstance(numerical_integratior, NumericalIntegrator))

    def test_numerical_integratior_trapezium_method_func_zero(self):
        def func(x):
            return 0
        result = NumericalIntegrator().trapezium_method(1, 2, func)
        self.assertEqual(result, 0)

    def test_numerical_integratior_trapezium_method_func_linear(self):
        def func(x):
            return x
        result = NumericalIntegrator().trapezium_method(1, 2, func)
        self.assertEqual(round(result, 5), round(1.5, 5))

    def test_numerical_integratior_trapezium_method_func_difficult(self):
        def func(x):
            return x * (x + 1) + 1
        result = NumericalIntegrator().trapezium_method(1, 2, func)
        self.assertEqual(round(result, 5), round(4.83333, 5))

    def test_numerical_integratior_trapezium_method_args_zero(self):
        def func(x):
            return x
        result = NumericalIntegrator().trapezium_method(0, 0, func)
        self.assertEqual(result, 0)

    def test_numerical_integratior_trapezium_method_args_positive_sub_negative(self):
        def func(x):
            return x
        result = NumericalIntegrator().trapezium_method(2, 1, func)
        self.assertEqual(round(result, 5), round(-1.5, 5))

    def test_numerical_integratior_trapezium_method_args_negative_sub_positive(self):
        def func(x):
            return x
        result = NumericalIntegrator().trapezium_method(-2, -1, func)
        self.assertEqual(round(result, 5), round(-1.5, 5))

    def test_numerical_integratior_trapezium_method_args_negative_sub_negative(self):
        def func(x):
            return x
        result = NumericalIntegrator().trapezium_method(-1, -2, func)
        self.assertEqual(round(result, 5), round(1.5, 5))

    def test_numerical_integratior_simpson_method_func_zero(self):
        def func(x):
            return 0
        result = NumericalIntegrator().simpson_method(1, 2, func)
        self.assertEqual(result, 0)

    def test_numerical_integratior_simpson_method_func_linear(self):
        def func(x):
            return x
        result = NumericalIntegrator().simpson_method(1, 2, func)
        self.assertEqual(round(result, 5), round(1.5, 5))

    def test_numerical_integratior_simpson_method_func_difficult(self):
        def func(x):
            return x * (x + 1) + 1
        result = NumericalIntegrator().simpson_method(1, 2, func)
        self.assertEqual(round(result, 5), round(4.83333, 5))

    def test_numerical_integratior_simpson_method_args_zero(self):
        def func(x):
            return x
        result = NumericalIntegrator().simpson_method(0, 0, func)
        self.assertEqual(result, 0)

    def test_numerical_integratior_simpson_method_args_positive_sub_negative(self):
        def func(x):
            return x
        result = NumericalIntegrator().simpson_method(2, 1, func)
        self.assertEqual(round(result, 5), round(-1.5, 5))

    def test_numerical_integratior_simpson_method_args_negative_sub_positive(self):
        def func(x):
            return x
        result = NumericalIntegrator().simpson_method(-2, -1, func)
        self.assertEqual(round(result, 5), round(-1.5, 5))

    def test_numerical_integratior_simpson_method_args_negative_sub_negative(self):
        def func(x):
            return x
        result = NumericalIntegrator().simpson_method(-1, -2, func)
        self.assertEqual(round(result, 5), round(1.5, 5))
