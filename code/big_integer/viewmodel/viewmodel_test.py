import unittest

from big_integer.viewmodel.viewmodel import BigIntegerViewModel, CalculateState, Operation
from big_integer.logger.fakelogger import FakeLogger
from big_integer.logger.reallogger import RealLogger


class TestBigIntegerViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = BigIntegerViewModel()

    def test_by_default_config(self):
        self.assertEqual("456", self.view_model.get_a())
        self.assertEqual("123", self.view_model.get_b())
        self.assertEqual(Operation.ADDITIONAL, self.view_model.get_operation())
        self.assertEqual(CalculateState.ENABLE, self.view_model.get_calculate_state())
        self.assertEqual("579", self.view_model.get_result())

    def test_when_entered_valid_a_b_button_enabled(self):
        self.view_model.set_a("489485")
        self.view_model.set_b("845121214587")
        self.assertEqual(CalculateState.ENABLE, self.view_model.get_calculate_state())

    def test_when_entered_invalid_a_button_disabled(self):
        self.view_model.set_a("489ewr485")
        self.view_model.set_b("845121214587")
        self.assertEqual(CalculateState.DISABLE, self.view_model.get_calculate_state())

    def test_when_entered_invalid_b_button_disabled(self):
        self.view_model.set_a("489485")
        self.view_model.set_b("8455sa4587")
        self.assertEqual(CalculateState.DISABLE, self.view_model.get_calculate_state())

    def test_can_retrieve_a_text(self):
        self.view_model.set_a("23153")
        self.assertEqual("23153", self.view_model.get_a())

    def test_can_retrieve_b_text(self):
        self.view_model.set_b("45487")
        self.assertEqual("45487", self.view_model.get_b())

    def test_can_retrieve_a_text_invalid(self):
        self.view_model.set_a("2eee3153")
        self.assertEqual("2eee3153", self.view_model.get_a())

    def test_can_retrieve_b_text_invalid(self):
        self.view_model.set_b("45ddd487")
        self.assertEqual("45ddd487", self.view_model.get_b())

    def test_can_retrieve_a_text_zero(self):
        self.view_model.set_a("0")
        self.assertEqual("0", self.view_model.get_a())

    def test_can_retrieve_b_text_zero(self):
        self.view_model.set_b("0")
        self.assertEqual("0", self.view_model.get_b())

    def test_can_retrieve_operation_text(self):
        self.view_model.set_operation(Operation.MULTIPLICATION)
        self.assertEqual(Operation.MULTIPLICATION, self.view_model.get_operation())

    def test_when_entered_a_b_then_clear_a_button_disabled(self):
        self.view_model.set_a("21312")
        self.view_model.set_b("5454578")
        self.view_model.set_a("")
        self.assertEqual(CalculateState.DISABLE, self.view_model.get_calculate_state())

    def test_when_entered_a_b_then_clear_b_button_disabled(self):
        self.view_model.set_a("21312")
        self.view_model.set_b("5454578")
        self.view_model.set_b("")
        self.assertEqual(CalculateState.DISABLE, self.view_model.get_calculate_state())

    def test_when_entered_a_b_then_clear_a_b_button_disabled(self):
        self.view_model.set_a("21312")
        self.view_model.set_b("5454578")
        self.view_model.set_a("")
        self.view_model.set_b("")
        self.assertEqual(CalculateState.DISABLE, self.view_model.get_calculate_state())

    def test_can_get_add(self):
        self.view_model.set_a("1111111")
        self.view_model.set_b("222")
        self.view_model.set_operation(Operation.ADDITIONAL)
        self.view_model.calculate()
        self.assertEqual("1111333", self.view_model.get_result())

    def test_can_get_sub(self):
        self.view_model.set_a("2222222")
        self.view_model.set_b("111")
        self.view_model.set_operation(Operation.SUBTRACTION)
        self.view_model.calculate()
        self.assertEqual("2222111", self.view_model.get_result())

    def test_can_get_mul(self):
        self.view_model.set_a("3546")
        self.view_model.set_b("87854545454")
        self.view_model.set_operation(Operation.MULTIPLICATION)
        self.view_model.calculate()
        self.assertEqual("311532218179884", self.view_model.get_result())

    def test_can_result_zero(self):
        self.view_model.set_a("0")
        self.view_model.set_b("0")
        self.view_model.set_operation(Operation.ADDITIONAL)
        self.view_model.calculate()
        self.assertEqual("0", self.view_model.get_result())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = BigIntegerViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Hello', self.view_model.logger.get_last_message())

    def test_logging_changing_a_correct(self):
        expected_messages = ['Hello',
                             'Input a: 555',
                             'Correct input a']

        self.view_model.set_a("555")
        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages())

    def test_logging_changing_b_correct(self):
        expected_messages = ['Hello',
                             'Input b: 666',
                             'Correct input b']

        self.view_model.set_b("666")
        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages())

    def test_logging_changing_a_invalid(self):
        expected_messages = ['Hello',
                             'Input a: wer',
                             'Invalid input a']

        self.view_model.set_a("wer")
        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages())

    def test_logging_changing_b_invalid(self):
        expected_messages = ['Hello',
                             'Input b: ref',
                             'Invalid input b']

        self.view_model.set_b("ref")
        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages())

    def test_logging_performing_operation(self):
        expected_messages = ['Hello',
                             'Input a: 456',
                             'Correct input a',
                             'Input b: 123',
                             'Correct input b',
                             'Set operation: Operation.ADDITIONAL',
                             'Button clicked',
                             'Operation: Operation.ADDITIONAL',
                             'Result: 579']

        self.view_model.set_a("456")
        self.view_model.set_b("123")
        self.view_model.set_operation(Operation.ADDITIONAL)
        self.view_model.calculate()
        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages())


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = BigIntegerViewModel(RealLogger())
