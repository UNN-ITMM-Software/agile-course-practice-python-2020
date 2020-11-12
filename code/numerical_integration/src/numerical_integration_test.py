import unittest

from numerical_integration import NumericalIntegrator

class TestNumericalIntegratorClass(unittest.TestCase):
    def test_numerical_integratior_can_create(self):
        numericalIntegratior = NumericalIntegrator()
        self.assertTrue(isinstance(numericalIntegratior, NumericalIntegrator))

    def test_numerical_integratior_trapeziumMethod_func_zero(self):
        def func(x): 
            return 0
        result = NumericalIntegrator().trapeziumMethod(1, 2, func)
        self.assertEqual(result, 0)

    def test_numerical_integratior_trapeziumMethod_func_linear(self):
        def func(x): 
            return x
        result = NumericalIntegrator().trapeziumMethod(1, 2, func)
        self.assertEqual(round(result,5), round(1.5,5))

    def test_numerical_integratior_trapeziumMethod_func_difficult(self):
        def func(x): 
            return x * (x + 1) + 1
        result = NumericalIntegrator().trapeziumMethod(1, 2, func)
        self.assertEqual(round(result, 5), round(4.83333, 5))

    def test_numerical_integratior_trapeziumMethod_args_zero(self):
        def func(x): 
            return x
        result = NumericalIntegrator().trapeziumMethod(0, 0, func)
        self.assertEqual(result, 0)

    def test_numerical_integratior_trapeziumMethod_args_positive_sub_negative(self):
        def func(x): 
            return x
        result = NumericalIntegrator().trapeziumMethod(2, 1, func)
        self.assertEqual(round(result,5), round(-1.5,5))

    def test_numerical_integratior_trapeziumMethod_args_negative_sub_positive(self):
        def func(x): 
            return x
        result = NumericalIntegrator().trapeziumMethod(-2, -1, func)
        self.assertEqual(round(result,5), round(-1.5,5))

    def test_numerical_integratior_trapeziumMethod_args_negative_sub_negative(self):
        def func(x): 
            return x
        result = NumericalIntegrator().trapeziumMethod(-1, -2, func)
        self.assertEqual(round(result,5), round(1.5,5))
