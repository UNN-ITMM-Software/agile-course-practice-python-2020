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

    def test_set_button_state_changes_state_true(self):
        self.viewmodel.set_button_state('active')
        self.assertEqual('active', self.viewmodel.get_button_state())
