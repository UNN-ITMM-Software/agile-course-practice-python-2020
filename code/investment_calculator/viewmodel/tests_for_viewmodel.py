import unittest

from investment_calculator.viewmodel.viewmodel import InvestmentCalculatorViewModel

from investment_calculator.logger.fakelogger import FakeLogger
from investment_calculator.logger.reallogger import RealLogger


class TestStatisticsViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = InvestmentCalculatorViewModel(FakeLogger())

    def test_by_default_button_normal(self):
        self.assertEqual('normal', self.view_model.get_button_convert_state())

    def test_can_get_input_string_1(self):
        self.view_model.set_instr("1", "2", "3", "4")
        self.assertEqual("1", self.view_model.get_R_txt())

    def test_can_get_input_string_2(self):
        self.view_model.set_instr("1", "2", "3", "4")
        self.assertEqual("2", self.view_model.get_K_txt())

    def test_can_get_input_string_3(self):
        self.view_model.set_instr("1", "2", "3", "4")
        self.assertEqual("3", self.view_model.get_n_txt())

    def test_can_get_input_string_4(self):
        self.view_model.set_instr("1", "2", "3", "4")
        self.assertEqual("4", self.view_model.get_q_txt())

    def test_can_get_answer1(self):
        self.view_model.set_instr("1", "2", "3", "4")
        self.view_model.click_button()
        self.assertEqual(-1.752, self.view_model.get_answer())

    def test_can_get_answer2(self):
        self.view_model.set_instr("100.1", "500.1", "10.1", "0.1")
        self.view_model.click_button()
        self.assertEqual(118.63198853578206, self.view_model.get_answer())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = InvestmentCalculatorViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome to net present value calculator!',
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
        self.view_model.set_instr("2", "1", "4", "3")
        self.assertEqual('Entered data: R=1, K=2, q=3, n=4',
                         self.view_model.logger.get_last_message())

    def test_logging_result(self):
        self.view_model.set_instr("2", "1", "4", "3")
        self.view_model.click_button()

        last_messages = ['Button clicked', 'Result: -0.3359375']
        self.assertEqual(last_messages, self.view_model.logger.get_log_messages()[-2:])


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = InvestmentCalculatorViewModel(RealLogger())
