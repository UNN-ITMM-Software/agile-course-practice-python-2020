import unittest

from logger.fakelogger import FakeLogger
from logger.reallogger import RealLogger
from viewmodel import ViewModel


class TestFractionCalculatorViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = ViewModel(FakeLogger())

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_both_fractions_button_enabled(self):
        self.view_model.set_first_fraction('1')
        self.view_model.set_second_fraction('1')
        self.assertNotEqual('disabled', self.view_model.get_button_convert_state())

    def test_can_retrieve_fractions_text(self):
        self.view_model.set_first_fraction('1')
        self.view_model.set_second_fraction('1')
        actual_fraction_1 = self.view_model.get_first_fraction()
        actual_fraction_2 = self.view_model.get_second_fraction()

        self.assertEqual('1', actual_fraction_1)
        self.assertEqual('1', actual_fraction_2)

    def test_when_entered_both_fractions_then_clear_one_button_disabled(self):
        self.view_model.set_first_fraction('1')
        self.view_model.set_second_fraction('1')
        self.view_model.set_first_fraction('')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_not_frac_button_disabled(self):
        self.view_model.set_first_fraction('1')
        self.view_model.set_second_fraction('1a')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_can_add_1_and_1(self):
        self.view_model.set_first_fraction('1')
        self.view_model.set_second_fraction('1')
        self.view_model.click_convert()
        self.assertEqual('2/1', self.view_model.get_msg_text())

    def test_can_substract_1_and_1(self):
        self.view_model.set_first_fraction('1')
        self.view_model.set_second_fraction('1')
        self.view_model.set_operation('-')
        self.view_model.click_convert()
        self.assertEqual('0/1', self.view_model.get_msg_text())

    def test_can_divide_2_3_and_3_2(self):
        self.view_model.set_first_fraction('2/3')
        self.view_model.set_second_fraction('3/2')
        self.view_model.set_operation('/')
        self.view_model.click_convert()
        self.assertEqual('4/9', self.view_model.get_msg_text())

    def test_cannot_divide_by_0(self):
        self.view_model.set_first_fraction('2/3')
        self.view_model.set_second_fraction('0')
        self.view_model.set_operation('/')
        self.view_model.click_convert()
        self.assertEqual('Error! Cannot divide by zero!',
                         self.view_model.get_msg_text())

    def test_can_multiply_2_3_and_2_3(self):
        self.view_model.set_first_fraction('2/3')
        self.view_model.set_second_fraction('2/3')
        self.view_model.set_operation('*')
        self.view_model.click_convert()
        self.assertEqual('4/9', self.view_model.get_msg_text())

    def test_by_default_second_text_is_enabled(self):
        self.assertEqual('normal', self.view_model.get_second_fraction_text_state())

    def test_when_selected_continuous_second_text_is_disabled(self):
        self.view_model.set_first_fraction('2/3')
        self.view_model.set_operation('Convert to continuous')
        self.assertEqual('disabled',
                         self.view_model.get_second_fraction_text_state())

    def test_when_selected_continuous_then_plus_second_text_is_enabled(self):
        self.view_model.set_first_fraction('2/3')
        self.view_model.set_operation('Convert to continuous')
        self.view_model.set_operation('+')
        self.assertEqual('normal',
                         self.view_model.get_second_fraction_text_state())

    def test_can_convert_1_to_continuous(self):
        self.view_model.set_first_fraction('1')
        self.view_model.set_operation('Convert to continuous')
        self.view_model.click_convert()
        self.assertEqual(str([1]), self.view_model.get_msg_text())

    def test_can_convert_2_to_continuous(self):
        self.view_model.set_first_fraction('2/3')
        self.view_model.set_operation('Convert to continuous')
        self.view_model.click_convert()
        self.assertEqual(str([0, 1, 2]), self.view_model.get_msg_text())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = ViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome!', self.view_model.logger.get_last_message())

    def test_logging_changing_first_fraction(self):
        self.view_model.set_first_fraction('2/3')
        self.assertEqual('Setting first fraction to 2/3', self.view_model.logger.get_last_message())

    def test_logging_changing_second_fraction(self):
        self.view_model.set_second_fraction('2/3')
        self.assertEqual('Setting second fraction to 2/3', self.view_model.logger.get_last_message())

    def test_logging_changing_operation(self):
        self.view_model.set_second_fraction('2/3')
        self.view_model.set_operation('Convert to continuous')
        self.assertEqual('Setting operation to: Convert to continuous',
                         self.view_model.logger.get_last_message())

    def test_logging_performing_operation(self):
        expected_messages = ['Button clicked', 'Selected operation is *', 'Result: 4/9']

        self.view_model.set_first_fraction('2/3')
        self.view_model.set_second_fraction('2/3')
        self.view_model.set_operation('*')
        self.view_model.click_convert()

        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages()[-3:])


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = ViewModel(RealLogger())
