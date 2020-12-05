import unittest

from float_vector_metrics.viewmodel.viewmodel import VectorMetricsViewModel


class TestVectorMetricsViewModel(unittest.TestCase):
    def setUp(self):
        self.viewmodel = VectorMetricsViewModel()

    def test_button_disabled_by_default(self):
        self.assertEqual('disabled', self.viewmodel.get_button_state())

    def test_button_enabled_when_metric_set(self):
        self.viewmodel.set_metric('L1')
        self.assertEqual('active', self.viewmodel.get_button_state())

    def test_button_disabled_when_x_value_erased(self):
        self.viewmodel.set_x('')
        self.assertEqual('disabled', self.viewmodel.get_button_state())

    def test_button_disabled_when_incorrect_x_value(self):
        self.viewmodel.set_x('!')
        self.assertEqual('disabled', self.viewmodel.get_button_state())

    def test_error_message_on_incorrect_value(self):
        self.viewmodel.set_y('!')
        self.assertEqual('Error: Incorrect expression, only list notations supported',
                         self.viewmodel.get_error_message())

    def test_button_enabled_when_correct_x_value(self):
        self.viewmodel.set_x('[1, 2, 3]')
        self.assertEqual('active', self.viewmodel.get_button_state())

    def test_error_message_is_empty_on_correct_value(self):
        self.viewmodel.set_y('[1, 2, 3]')
        self.assertEqual('', self.viewmodel.get_error_message())

    def test_can_change_x_value(self):
        self.viewmodel.set_x('[3, 2, 1]')
        self.assertEqual('[3, 2, 1]', self.viewmodel.get_x())

    def test_can_change_y_value(self):
        self.viewmodel.set_y('[4, 5, 1]')
        self.assertEqual('[4, 5, 1]', self.viewmodel.get_y())

    def test_error_message_is_shown_when_length_unequal(self):
        self.viewmodel.set_x('[1, 2, 3]')
        self.viewmodel.set_y('[1, 2, 3, 4]')
        self.viewmodel.set_metric('L1')
        self.viewmodel.compute()
        self.assertEqual('Error: Vectors of different lengths obtained. Distance can only be '
                         'calculated between vectors of equal length.',
                         self.viewmodel.get_error_message())

    def test_can_compute_metric(self):
        self.viewmodel.set_x('[1.2, 1.5, 1.8]')
        self.viewmodel.set_y('[2.2, 2.5, 2.8]')
        self.viewmodel.set_metric('L1')
        self.viewmodel.compute()
        self.assertEqual('Result: 3.0', self.viewmodel.get_result())
