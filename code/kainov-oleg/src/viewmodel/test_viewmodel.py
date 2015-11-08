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

    def test_when_entered_both_fractions_then_clear_one_button_disabled(self):
        view_model = ViewModel()
        view_model.set_first_fraction('1')
        view_model.set_second_fraction('1')
        view_model.set_first_fraction('')
        self.assertEqual('disabled', view_model.get_button_convert_state())

    def test_when_entered_not_frac_button_disabled(self):
        view_model = ViewModel()
        view_model.set_first_fraction('1')
        view_model.set_second_fraction('1a')
        self.assertEqual('disabled', view_model.get_button_convert_state())

    def test_can_add_1_and_1(self):
        view_model = ViewModel()
        view_model.set_first_fraction('1')
        view_model.set_second_fraction('1')
        view_model.click_convert()
        self.assertEqual('2/1', view_model.get_msg_text())
