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

    def test_can_retrieve_fractions_text(self):
        view_model = ViewModel()
        view_model.set_first_fraction('1')
        view_model.set_second_fraction('1')
        actual_fraction_1 = view_model.get_first_fraction()
        actual_fraction_2 = view_model.get_second_fraction()

        self.assertEqual('1', actual_fraction_1)
        self.assertEqual('1', actual_fraction_2)

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

    def test_can_substract_1_and_1(self):
        view_model = ViewModel()
        view_model.set_first_fraction('1')
        view_model.set_second_fraction('1')
        view_model.set_operation('-')
        view_model.click_convert()
        self.assertEqual('0/1', view_model.get_msg_text())

    def test_can_divide_2_3_and_3_2(self):
        view_model = ViewModel()
        view_model.set_first_fraction('2/3')
        view_model.set_second_fraction('3/2')
        view_model.set_operation('/')
        view_model.click_convert()
        self.assertEqual('4/9', view_model.get_msg_text())

    def test_can_multiply_2_3_and_2_3(self):
        view_model = ViewModel()
        view_model.set_first_fraction('2/3')
        view_model.set_second_fraction('2/3')
        view_model.set_operation('*')
        view_model.click_convert()
        self.assertEqual('4/9', view_model.get_msg_text())

    def test_by_default_second_text_is_enabled(self):
        view_model = ViewModel()
        self.assertEqual('normal', view_model.get_second_fraction_text_state())

    def test_when_selected_continuous_second_text_is_disabled(self):
        view_model = ViewModel()
        view_model.set_first_fraction('2/3')
        view_model.set_operation('Convert to continuous')
        self.assertEqual('disabled',
                         view_model.get_second_fraction_text_state())

    def test_when_selected_continuous_then_plus_second_text_is_enabled(self):
        view_model = ViewModel()
        view_model.set_first_fraction('2/3')
        view_model.set_operation('Convert to continuous')
        view_model.set_operation('+')
        self.assertEqual('normal',
                         view_model.get_second_fraction_text_state())

    def test_can_convert_1_to_continuous(self):
        view_model = ViewModel()
        view_model.set_first_fraction('1')
        view_model.set_operation('Convert to continuous')
        view_model.click_convert()
        self.assertEqual(str([1]), view_model.get_msg_text())

    def test_can_convert_2_to_continuous(self):
        view_model = ViewModel()
        view_model.set_first_fraction('2/3')
        view_model.set_operation('Convert to continuous')
        view_model.click_convert()
        self.assertEqual(str([0, 1, 2]), view_model.get_msg_text())
