import unittest

from statistics.viewmodel.viewmodel import StatisticsViewModel


class TestStatisticsViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = StatisticsViewModel()

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_valid_string_button_enabled(self):
        self.view_model.set_instr("5 5")
        self.assertNotEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_invalid_string_button_disabled(self):
        self.view_model.set_instr("1+2")
        self.assertNotEqual('normal', self.view_model.get_button_convert_state())

    def test_can_get_input_string(self):
        self.view_model.set_instr("1,2")
        instr = self.view_model.get_instr()
        self.assertEqual("1,2", instr)

    def test_can_get_answer(self):
        self.view_model.set_instr("2 2")
        self.view_model.click_button()
        self.assertEqual(0, self.view_model.get_answer())
