
import unittest

from lcd_digits.view_model.view_model import LcdDigitViewModel


class TestLcdDigitViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = LcdDigitViewModel()

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
