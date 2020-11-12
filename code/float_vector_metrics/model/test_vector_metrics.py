import unittest

from float_vector_metrics.model.float_vector_metrics import VectorMetrics


class TestVectorMetricsClass(unittest.TestCase):

    def test_can_create_class(self):
        metrics_calc = VectorMetrics()
        self.assertTrue(isinstance(metrics_calc, VectorMetrics))

    def test_can_calculate_l1_metric(self):
        a = [1.2, 1.5, 1.8]
        b = [2.2, 2.5, 2.8]
        metrics_calculator = VectorMetrics()
        calc_value = metrics_calculator.l1(a, b)
        self.assertEqual(calc_value, 3)

    def test_can_calculate_l2_metric(self):
        a = [1.2, 1.5, 1.8]
        b = [1.3, 1.4, 1.7]
        metrics_calculator = VectorMetrics()
        calc_value = metrics_calculator.l2(a, b)
        self.assertAlmostEqual(calc_value, 0.17320508)

    def test_can_calculate_l3_metric(self):
        a = [1.2, 1.5, 1.8]
        b = [5.2, 7.5, 1.7]
        metrics_calculator = VectorMetrics()
        calc_value = metrics_calculator.l3(a, b)
        self.assertAlmostEqual(calc_value, 6.5421404)

    def test_can_calculate_l4_metric(self):
        a = [1.2, 1.8, 1.4]
        b = [1.2, 1.4, 1.8]
        metrics_calculator = VectorMetrics()
        calc_value = metrics_calculator.l4(a, b)
        self.assertAlmostEqual(calc_value, 0.4756828)

    def test_can_calculate_linf_metric(self):
        a = [1.2, 1.5, 1.8]
        b = [3.3, 8.7, 1.7]
        metrics_calculator = VectorMetrics()
        calc_value = metrics_calculator.l4(a, b)
        self.assertAlmostEqual(calc_value, 7.2129911)

    def test_can_raise_error_when_vector_not_list(self):
        a = [1.2, 1.5, 1.8]
        b = 5
        metrics_calculator = VectorMetrics()
        with self.assertRaises(TypeError):
            metrics_calculator.l4(a, b)

    def test_can_raise_error_when_vector_of_equal_length(self):
        a = [1.2, 1.5, 1.8]
        b = [5]
        metrics_calculator = VectorMetrics()
        with self.assertRaises(ValueError):
            metrics_calculator.l3(a, b)
