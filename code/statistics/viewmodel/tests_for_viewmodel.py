import unittest

from statistics.viewmodel.viewmodel import StatisticsViewModel

from statistics.logger.fakelogger import FakeLogger
from statistics.logger.reallogger import RealLogger


class TestStatisticsViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = StatisticsViewModel(FakeLogger())

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_valid_string_button_enabled(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        self.view_model.validate_text()
        self.assertEqual('normal', self.view_model.get_button_convert_state())

    def test_when_entered_invalid_string_button_disabled(self):
        self.view_model.set_instr("5+5", "5 5", "5 5")
        self.view_model.validate_text()
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_can_get_input_string_student_1(self):
        self.view_model.set_instr("1 1", "3 3", "5 5")
        self.assertEqual("1 1", self.view_model.get_marks1_txt())

    def test_can_get_input_string_student_2(self):
        self.view_model.set_instr("1 1", "3 3", "5 5")
        self.assertEqual("3 3", self.view_model.get_marks2_txt())

    def test_can_get_input_string_student_3(self):
        self.view_model.set_instr("1 1", "3 3", "5 5")
        self.assertEqual("5 5", self.view_model.get_marks3_txt())

    def test_add_empty_string_is_0(self):
        self.view_model.set_instr("", "", "")
        self.view_model.validate_text()
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_invalid_string(self):
        self.view_model.set_instr("1 f", "3 3", "5 5")
        self.view_model.validate_text()
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_add_empty_string_after_correct_input(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        self.view_model.validate_text()
        self.view_model.set_instr("", "", "")
        self.view_model.validate_text()
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_add_negative_marks(self):
        self.view_model.set_instr("5 5", "-5 -5", "5 5")
        self.view_model.validate_text()
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_add_marks_over_5(self):
        self.view_model.set_instr("0 1", "2 3", "4 5")
        self.view_model.validate_text()
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_can_get_answer1(self):
        self.view_model.set_instr("1 1", "3 3", "5 5")
        self.view_model.validate_text()
        self.view_model.click_button()
        self.assertEqual(1, self.view_model.get_answer_losers())

    def test_can_get_answer2(self):
        self.view_model.set_instr("1 1", "3 3", "5 5")
        self.view_model.validate_text()
        self.view_model.click_button()
        self.assertEqual(1, self.view_model.get_answer_successfully())

    def test_can_get_answer3(self):
        self.view_model.set_instr("1 1", "3 3", "5 5")
        self.view_model.validate_text()
        self.view_model.click_button()
        self.assertEqual(1, self.view_model.get_answer_excellent())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = StatisticsViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome to academic performance calculator!',
                         self.view_model.logger.get_last_message())

    def test_logging_set_button_disabled(self):
        self.view_model.set_btn_disabled()
        self.assertEqual('Button state was set to "disabled"',
                         self.view_model.logger.get_last_message())

    def test_logging_set_button_enabled(self):
        self.view_model.set_btn_enabled()
        self.assertEqual('Button state was set to "normal"',
                         self.view_model.logger.get_last_message())

    def test_logging_set_instr(self):
        self.view_model.set_instr("0 1", "2 3", "4 5")
        self.assertEqual('Entered marks: 0 1, 2 3, 4 5',
                         self.view_model.logger.get_last_message())

    def test_logging_valid_input(self):
        self.view_model.set_instr("1 1", "3 3", "5 5")
        self.view_model.validate_text()
        self.assertEqual('Marks was successfully written: "[1, 1]", "[3, 3]", "[5, 5]"',
                         self.view_model.logger.get_last_message())

    def test_logging_invalid_input(self):
        self.view_model.set_instr("1 A", "-3 3", "0 6")
        self.view_model.validate_text()
        self.assertEqual('Invalid input!',
                         self.view_model.logger.get_last_message())

    def test_logging_result(self):
        self.view_model.set_instr("1 1", "3 3", "5 5")
        self.view_model.validate_text()
        self.view_model.click_button()

        last_messages = ['Button clicked', 'Result: 1, 1, 1']
        self.assertEqual(last_messages, self.view_model.logger.get_log_messages()[-2:])


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = StatisticsViewModel(RealLogger())
