import unittest

from string_calculator.viewmodel.viewmodel import StrCalculatorViewModel


class TestStringCalculatorViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = StrCalculatorViewModel()

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_valid_string_button_enabled(self):
        self.view_model.set_instr("1,2")
        self.assertNotEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_invalid_string_button_disabled(self):
        self.view_model.set_instr("1+2")
        self.assertNotEqual('normal', self.view_model.get_button_convert_state())

    def test_can_get_input_string(self):
        self.view_model.set_instr("1,2")
        instr = self.view_model.get_instr()
        self.assertEqual("1,2", instr)

    def test_can_get_answer(self):
        self.view_model.set_instr("1,2")
        self.view_model.click_button()
        self.assertEqual(3, self.view_model.get_answer())

    def test_add_empty_string_is_0(self):
        self.view_model.set_instr("")
        self.view_model.click_button()
        self.assertEqual(0, self.view_model.get_answer())

    def test_add_string_1(self):
        self.view_model.set_instr("1")
        self.view_model.click_button()
        self.assertEqual(1, self.view_model.get_answer())

    def test_add_strings_1_2(self):
        self.view_model.set_instr("1,2")
        self.view_model.click_button()
        self.assertEqual(3, self.view_model.get_answer())

    def test_can_add_unknown_amount_strings(self):
        self.view_model.set_instr("2,3,1,0,5,6,0,1,2")
        self.view_model.click_button()
        self.assertEqual(20, self.view_model.get_answer())

    def test_can_use_newline_delimiter(self):
        self.view_model.set_instr("1\n2,3")
        self.view_model.click_button()
        self.assertEqual(6, self.view_model.get_answer())

    def test_can_use_newline_delimiter_mix(self):
        self.view_model.set_instr("1\n2,3,4\n5,6\n7")
        self.view_model.click_button()
        self.assertEqual(28, self.view_model.get_answer())

    def test_can_use_custom_delimiter(self):
        self.view_model.set_instr(";\n1;2")
        self.view_model.click_button()
        self.assertEqual(3, self.view_model.get_answer())

    def test_can_use_custom_delimiter_hard(self):
        self.view_model.set_instr(";\n1;2;3;4;5;6;7")
        self.view_model.click_button()
        self.assertEqual(28, self.view_model.get_answer())

    def test_check_negative_numbers_is_not_allowed(self):
        self.view_model.set_instr("-1,-2")
        msg = 'negatives not allowed: -1, -2'
        with self.assertRaisesRegex(ValueError, msg):
            self.view_model.click_button()
