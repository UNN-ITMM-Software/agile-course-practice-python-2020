import unittest

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
