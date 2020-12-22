import unittest

from deposit_calc.viewmodel.viewmodel import DepositCalcViewModel
from deposit_calc.logger.fakelogger import FakeLogger
from deposit_calc.logger.reallogger import RealLogger


class TestDepositCalcViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = DepositCalcViewModel()

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_handle_btn_state())

    def test_when_entered_correct_start_depo_button_enabled(self):
        self.view_model.set_start_depo('100000')
        self.assertNotEqual('disabled', self.view_model.get_handle_btn_state())

    def test_when_entered_correct_depo_time_button_enabled(self):
        self.view_model.set_depo_time('1.5')
        self.assertNotEqual('disabled', self.view_model.get_handle_btn_state())

    def test_when_entered_correct_rate_button_enabled(self):
        self.view_model.set_rate('0.05')
        self.assertNotEqual('disabled', self.view_model.get_handle_btn_state())

    def test_when_entered_correct_capitalization_freq_button_enabled(self):
        self.view_model.set_capitalization('4')
        self.assertNotEqual('disabled', self.view_model.get_handle_btn_state())

    def test_when_entered_correct_replenishment_freq_button_enabled(self):
        self.view_model.set_replenishment_freq('2')
        self.assertNotEqual('disabled', self.view_model.get_handle_btn_state())

    def test_when_entered_correct_replemishment_size_button_enabled(self):
        self.view_model.set_replenishment_size('10000')
        self.assertNotEqual('disabled', self.view_model.get_handle_btn_state())

    def test_can_retrieve_start_depo_text(self):
        self.view_model.set_start_depo('100000')
        start_depo = self.view_model.get_start_depo()
        self.assertEqual(100000.0, start_depo)

    def test_work_correctly_with_result(self):
        self.view_model.set_start_depo('100000')
        self.view_model.set_depo_time('1.5')
        self.view_model.set_rate('0.05')
        self.view_model.set_capitalization('4')
        self.view_model.set_replenishment_freq('2')
        self.view_model.set_replenishment_size('10000')
        self.view_model.handle_btn_clicked()
        self.assertEqual('8499', self.view_model.get_result())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = DepositCalcViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome!', self.view_model.logger.get_last_message())

    def test_logging_changing_start_deposit(self):
        self.view_model.set_start_depo('100000')
        self.assertEqual('Setting start deposit to 100000.0', self.view_model.logger.get_last_message())

    def test_logging_changing_deposit_time(self):
        self.view_model.set_depo_time('1.5')
        self.assertEqual('Setting deposit time to 1.5', self.view_model.logger.get_last_message())

    def test_logging_changing_interest_rate(self):
        self.view_model.set_rate('0.05')
        self.assertEqual('Setting interest rate to 0.05', self.view_model.logger.get_last_message())

    def test_logging_changing_capitalization_frequency(self):
        self.view_model.set_capitalization('4')
        self.assertEqual('Setting capitalization frequency to 4', self.view_model.logger.get_last_message())

    def test_logging_changing_replenishment_frequency(self):
        self.view_model.set_replenishment_freq('2')
        self.assertEqual('Setting replenishment frequency to 2', self.view_model.logger.get_last_message())

    def test_logging_changing_replenishment_size(self):
        self.view_model.set_replenishment_size('10000')
        self.assertEqual('Setting replenishment size to 10000', self.view_model.logger.get_last_message())

    def test_logging_performing_operation(self):
        expected_messages = ['Button clicked', 'Result: 8499']

        self.view_model.set_start_depo('100000')
        self.view_model.set_depo_time('1.5')
        self.view_model.set_rate('0.05')
        self.view_model.set_capitalization('4')
        self.view_model.set_replenishment_freq('2')
        self.view_model.set_replenishment_size('10000')
        self.view_model.handle_btn_clicked()

        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages()[-2:])


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = DepositCalcViewModel(RealLogger())
