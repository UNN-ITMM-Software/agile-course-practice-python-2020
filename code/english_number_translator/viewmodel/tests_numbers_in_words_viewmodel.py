import unittest

from english_number_translator.logger.fakelogger import FakeLogger
from english_number_translator.logger.reallogger import RealLogger
from english_number_translator.viewmodel.numbers_in_words_viewmodel import NumberInWordsViewModel


class TestNumberInWordsViewModel(unittest.TestCase):

    def test_default_button_is_disable(self):
        self.assertEqual('disabled', NumberInWordsViewModel().get_button_state())

    def test_when_enter_number_button_is_enable(self):
        model = NumberInWordsViewModel()
        model.set_number_value("1")
        self.assertEqual('normal', model.get_button_state())

    def test_when_empty_number_button_is_disable(self):
        model = NumberInWordsViewModel()
        model.set_number_value("")
        self.assertEqual('disabled', model.get_button_state())

    def test_when_enter_invalid_number_button_is_disable(self):
        model = NumberInWordsViewModel()
        model.set_number_value("fa1fa")
        self.assertEqual('disabled', model.get_button_state())

    def test_when_clear_number_button_is_disable(self):
        model = NumberInWordsViewModel()
        model.set_number_value("fa1fa")
        model.set_number_value("")
        self.assertEqual('disabled', model.get_button_state())

    def test_when_correct_invalid_number_button_is_enable(self):
        model = NumberInWordsViewModel()
        model.set_number_value("1fa")
        model.set_number_value("1")
        self.assertEqual('normal', model.get_button_state())

    def test_when_convert_1_display_one(self):
        model = NumberInWordsViewModel()
        model.set_number_value("1")
        model.click_convert()
        self.assertEqual('one', model.get_in_english())

    def test_when_clear_number_english_word_empty(self):
        model = NumberInWordsViewModel()
        model.set_number_value("1")
        model.click_convert()
        model.set_number_value("")
        self.assertEqual('', model.get_in_english())

    def test_when_enter_invalid_number_show_error(self):
        model = NumberInWordsViewModel()
        model.set_number_value("fa1fa")
        self.assertEqual('Only numbers', model.get_error_message())

    def test_when_clear_invalid_number_hide_error(self):
        model = NumberInWordsViewModel()
        model.set_number_value("fa1fa")
        model.set_number_value("")
        self.assertEqual('', model.get_error_message())

    def test_when_correct_invalid_number_hide_error(self):
        model = NumberInWordsViewModel()
        model.set_number_value("fa1fa")
        model.set_number_value("1")
        self.assertEqual('', model.get_error_message())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = NumberInWordsViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Starting...', self.view_model.logger.get_last_message())

    def test_logging_changing_number(self):
        self.view_model.set_number_value('123')
        self.assertEqual('Set number value to 123', self.view_model.logger.get_last_message())

    def test_logging_changing_number_to_incorrect(self):
        expected_messages = ['Set number value to 123a', 'Button was disabled']
        self.view_model.set_number_value('123a')
        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages()[-2:])

    def test_logging_changing_number_in_english(self):
        self.view_model.set_in_english('one hundred twenty-three')
        self.assertEqual('Set english number string to one hundred twenty-three',
                         self.view_model.logger.get_last_message())

    def test_logging_convert_number(self):
        expected_messages = ['Set number value to 123',
                             'Button was clicked',
                             'Set english number string to one hundred twenty-three']
        self.view_model.set_number_value('123')
        self.view_model.click_convert()
        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages()[-3:])


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = NumberInWordsViewModel(RealLogger())
