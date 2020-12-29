
import unittest

from lcd_digits.view_model.view_model import LcdDigitViewModel
from lcd_digits.model.lcd_digits_model import LcdDigitsModel
from lcd_digits.logger.fakelogger import FakeLogger
from lcd_digits.logger.reallogger import RealLogger


class TestLcdDigitViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = LcdDigitViewModel(FakeLogger())

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_digits_button_enabled(self):
        self.view_model.set_digits('10')
        self.assertNotEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_not_digits_button_not_enabled(self):
        self.view_model.set_digits('hello')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_negative_digits_button_not_enabled(self):
        self.view_model.set_digits('-520')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_decimal_number_button_not_enabled(self):
        self.view_model.set_digits('52.3')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_can_retrieve_digits_text(self):
        self.view_model.set_digits('10')
        digits = self.view_model.get_digits()

        self.assertEqual('10', digits)

    def test_when_entered_digits_then_clear_digits_button_disabled(self):
        self.view_model.set_digits('100')
        self.view_model.set_digits('')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_get_lcd_digits(self):
        self.view_model.set_digits('1')
        self.view_model.click_convert(26)
        self.assertEqual('... \n..| \n..| \n', self.view_model.get_msg_text())

    def test_get_string_from_lcd_digits(self):
        lcd_digits = LcdDigitsModel('1')
        self.assertEqual('... \n..| \n..| \n', LcdDigitViewModel.get_string(lcd_digits.lcd_numbers, 1000))


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = LcdDigitViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual(['LCD digit application is running.',
                          'Button is disabled.'],
                         self.view_model.logger.get_log_messages())

    def test_logging_set_digits(self):
        self.view_model.set_digits('100')
        self.assertEqual('digits set = 100',
                         self.view_model.logger.get_last_log_message())

    def test_logging_enable_button(self):
        self.view_model.set_btn_enabled()
        self.assertEqual('Button is enabled.',
                         self.view_model.logger.get_last_log_message())

    def test_logging_disable_button(self):
        self.view_model.set_btn_disabled()
        self.assertEqual('Button is disabled.',
                         self.view_model.logger.get_last_log_message())

    def test_logging_get_lcd_digit(self):
        expected_messages = ['LCD digit application is running.',
                             'Button is disabled.',
                             'Button is enabled.',
                             'digits set = 111',
                             'Button is clicked.',
                             'The answer:\n... ... ... \n..| ..| ..| \n..| ..| ..| \n']
        self.view_model.set_digits('111')
        self.view_model.click_convert(26)
        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages())

    def test_logging_get_lcd_digit_with_incorrect_value(self):
        self.view_model.set_digits('a10')
        self.view_model.click_convert(26)
        self.assertEqual(ValueError('Input error: wrong format').__str__(),
                         self.view_model.logger.get_last_log_message())


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = LcdDigitViewModel(RealLogger())
