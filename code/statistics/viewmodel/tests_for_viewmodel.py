import unittest

from statistics.logger.fakelogger import FakeLogger
from statistics.logger.reallogger import RealLogger
from statistics.viewmodel.viewmodel import StatisticsViewModel


class TestStatisticsViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = StatisticsViewModel()

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_valid_string_button_enabled(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        self.assertNotEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_invalid_string_button_disabled(self):
        self.view_model.set_instr("5+5", "5 5", "5 5")
        self.assertNotEqual('normal', self.view_model.get_button_convert_state())

    def test_can_get_input_string_1_student(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        instr = self.view_model.get_stud1_txt()
        self.assertEqual("5 5", instr)

    def test_can_get_input_string_2_student(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        instr = self.view_model.get_stud2_txt()
        self.assertEqual("5 5", instr)

    def test_can_get_input_string_3_student(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        instr = self.view_model.get_stud3_txt()
        self.assertEqual("5 5", instr)

    def test_can_get_answer1(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        self.view_model.click_button()
        self.assertEqual(0, self.view_model.get_answer_losers())

    def test_can_get_answer2(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        self.view_model.click_button()
        self.assertEqual(3, self.view_model.get_answer_successfully())

    def test_can_get_answer3(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        self.view_model.click_button()
        self.assertEqual(3, self.view_model.get_answer_excellent())

    def test_add_empty_string_is_0(self):
        self.view_model.set_instr("", "", "")
        self.assertNotEqual('normal', self.view_model.get_button_convert_state())

    def test_add_empty_string_after_correct_input(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        self.view_model.set_instr("", "", "")
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_add_negative_marks(self):
        self.view_model.set_instr("5 5", "-5 -5", "5 5")
        self.assertNotEqual('normal', self.view_model.get_button_convert_state())

    def test_add_marks_over_5(self):
        self.view_model.set_instr("5 7", "5 5", "5 5")
        self.assertNotEqual('normal', self.view_model.get_button_convert_state())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = StatisticsViewModel(FakeLogger())


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = StatisticsViewModel(RealLogger())
