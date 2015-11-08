import unittest

from viewmodel import ViewModel


class TestFractionCalculatorViewModel(unittest.TestCase):
    def test_by_default_button_disabled(self):
        view_model = ViewModel()
        self.assertEqual('disabled', view_model.get_button_convert_state())

    def test_when_entered_both_fractions_button_enabled(self):
        view_model = ViewModel()
        view_model.set_first_fraction('1')
        view_model.set_second_fraction('1')
        self.assertNotEqual('disabled', view_model.get_button_convert_state())
