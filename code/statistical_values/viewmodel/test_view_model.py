import unittest
from statistical_values.viewmodel.viewmodel import StatisticalValuesViewModel


class TestStatisticalValuesViewModel(unittest.TestCase):
    def setUp(self):
        self.viewmodel = StatisticalValuesViewModel()

    def test_can_set_k_value(self):
        self.viewmodel.set_k('3')
        self.assertEqual('3', self.viewmodel.get_k())

    def test_can_set_x_value(self):
        self.viewmodel.set_x('[1, 3, 2, 1]')
        self.assertEqual('[1, 3, 2, 1]', self.viewmodel.get_x())

    def test_button_disabled_by_default(self):
        self.assertEqual('disabled', self.viewmodel.get_button_state())

    def test_button_enabled_with_default_parameters_and_set_statistic(self):
        self.viewmodel.set_statistic('mean')
        self.assertEqual('active', self.viewmodel.get_button_state())

    def test_button_disabled_when_x_value_not_set(self):
        self.viewmodel.set_x('')
        self.assertEqual('disabled', self.viewmodel.get_button_state())

    def test_button_disabled_with_incorrect_x_value(self):
        self.viewmodel.set_x('[2, 3!')
        self.assertEqual('disabled', self.viewmodel.get_button_state())

    def test_button_enabled_with_correct_x_value(self):
        self.viewmodel.set_x('(1, 2, 3, 4, 9)')
        self.assertEqual('active', self.viewmodel.get_button_state())

    def test_button_disabled_when_k_value_not_set_with_moments_values(self):
        self.viewmodel.set_statistic('central moment')
        self.viewmodel.set_k('')
        self.assertEqual('disabled', self.viewmodel.get_button_state())

    def test_button_enabled_when_k_value_with_not_moments_values(self):
        self.viewmodel.set_k('')
        self.viewmodel.set_statistic('mean')
        self.assertEqual('active', self.viewmodel.get_button_state())

    def test_button_disabled_when_incorrect_k_value(self):
        self.viewmodel.set_statistic('central moment')
        self.viewmodel.set_k('-2x')
        self.assertEqual('disabled', self.viewmodel.get_button_state())

    def test_set_button_state_changes_state_true(self):
        self.viewmodel.set_button_state('active')
        self.assertEqual('active', self.viewmodel.get_button_state())

    def test_error_message_on_incorrect_x_values(self):
        self.viewmodel.set_x('[12, / 34, 1, 0, 3]')
        self.assertEqual('Error: incorrect expression in Values List', self.viewmodel.get_error_message())

    def test_error_message_on_incorrect_x_type(self):
        self.viewmodel.set_x('{3: 6, 5: 9}')
        self.assertEqual('Error: only list or tuple input supported in Values List',
                         self.viewmodel.get_error_message())

    def test_error_message_on_incorrect_k_value(self):
        self.viewmodel.set_k('x')
        self.assertEqual('Error: incorrect value k', self.viewmodel.get_error_message())

    def test_error_message_on_incorrect_k_type(self):
        self.viewmodel.set_k('[1, 2]')
        self.assertEqual('Error: only int or float input supported in k', self.viewmodel.get_error_message())

    def test_error_message_is_empty_on_correct_value(self):
        self.viewmodel.set_x('[1, 2, 3, 4]')
        self.assertEqual('', self.viewmodel.get_error_message())

    def test_can_compute_statistic(self):
        self.viewmodel.set_x('[1, 2, 3, 2]')
        self.viewmodel.set_statistic('variance')
        self.viewmodel.compute()
        self.assertEqual('Result: 0.5', self.viewmodel.get_result())

    def test_error_message_is_shown_when_catch_operation_throw(self):
        self.viewmodel.set_x('[1, 2, 13, 1]')
        self.viewmodel.set_k('-1')
        self.viewmodel.set_statistic('central moment')
        self.viewmodel.compute()
        self.assertEqual('Error: k must be > 0', self.viewmodel.get_error_message())
