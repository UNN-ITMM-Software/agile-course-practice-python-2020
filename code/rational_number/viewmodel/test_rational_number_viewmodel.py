import unittest

from rational_number.viewmodel.rational_number_viewmodel import RationalNumberViewModel
from rational_number.logger.fakelogger import FakeLogger
from rational_number.logger.reallogger import RealLogger


class TestRationalNumberViewModel(unittest.TestCase):

    def test_calculate_button_disabled_by_default(self):
        viewmodel = RationalNumberViewModel()
        self.assertEqual("disabled", viewmodel.get_calculate_button_state())

    def test_numbers_filled_calculate_button_enabled(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("1/2")
        viewmodel.set_second_number("2/7")
        self.assertEqual("normal", viewmodel.get_calculate_button_state())

    def test_numbers_filled_and_removed_calculate_button_disabled(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("1/2")
        viewmodel.set_second_number("2/7")
        viewmodel.set_second_number("")
        self.assertEqual("disabled", viewmodel.get_calculate_button_state())

    def test_numbers_invalid_calculate_button_disabled(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("a")
        viewmodel.set_second_number("2/7")
        self.assertEqual("disabled", viewmodel.get_calculate_button_state())

    def test_first_valid_second_valid_info_empty(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("12/3")
        viewmodel.set_second_number("2/7")
        self.assertEqual("", viewmodel.get_info_message())

    def test_first_empty_second_empty_info_correct(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("")
        viewmodel.set_second_number("")
        self.assertEqual("First number is empty.Second number is empty.", viewmodel.get_info_message())

    def test_first_valid_second_empty_info_correct(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("3/4")
        viewmodel.set_second_number("")
        self.assertEqual("Second number is empty.", viewmodel.get_info_message())

    def test_first_invalid_second_valid_info_correct(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("aaa")
        viewmodel.set_second_number("3/4")
        self.assertEqual("First number is invalid.", viewmodel.get_info_message())

    def test_first_invalid_second_invalid_info_correct(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("aaa")
        viewmodel.set_second_number("bbbb")
        self.assertEqual("First number is invalid.Second number is invalid.", viewmodel.get_info_message())

    def test_operation_invalid_calculate_button_disabled(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_operation("%")
        self.assertEqual("disabled", viewmodel.get_calculate_button_state())

    def test_first_valid_second_valid_plus_calculate(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("12/3")
        viewmodel.set_second_number("2/7")
        viewmodel.set_operation("+")
        viewmodel.calculate()
        self.assertEqual("30/7", viewmodel.get_result())

    def test_first_valid_second_valid_minus_calculate(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("12/3")
        viewmodel.set_second_number("2/7")
        viewmodel.set_operation("-")
        viewmodel.calculate()
        self.assertEqual("26/7", viewmodel.get_result())

    def test_first_valid_second_valid_mult_calculate(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("12/3")
        viewmodel.set_second_number("2/7")
        viewmodel.set_operation("*")
        viewmodel.calculate()
        self.assertEqual("8/7", viewmodel.get_result())

    def test_first_valid_second_valid_div_calculate(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("12/3")
        viewmodel.set_second_number("2/7")
        viewmodel.set_operation("/")
        viewmodel.calculate()
        self.assertEqual("14", viewmodel.get_result())

    def test_denominator_of_number_zero_calculate_button_disabled(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("12/0")
        viewmodel.set_second_number("2/7")
        viewmodel.set_operation("+")
        self.assertEqual("disabled", viewmodel.get_calculate_button_state())

    def test_denominators_of_numbers_are_zero_info_message_correct(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("13/0")
        viewmodel.set_second_number("7/0")
        self.assertEqual("Denominator of first number is zero.Denominator of second number is zero.",
                         viewmodel.get_info_message())

    def test_number_updated_result_empty(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("12/3")
        viewmodel.set_second_number("2/7")
        viewmodel.set_operation("+")
        viewmodel.calculate()
        viewmodel.set_first_number("12/11")
        self.assertEqual("", viewmodel.get_result())

    def test_operation_division_second_numerator_zero_calculate_button_disabled(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("12/3")
        viewmodel.set_second_number("0/1")
        viewmodel.set_operation("/")
        self.assertEqual("disabled", viewmodel.get_calculate_button_state())

    def test_operation_division_second_numerator_zero_info_message_correct(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("12/3")
        viewmodel.set_second_number("0/1")
        viewmodel.set_operation("/")
        self.assertEqual("Numerator of second number is zero. Division by zero is not allowed.",
                         viewmodel.get_info_message())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = RationalNumberViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual("Start view",
                         self.view_model.logger.get_last_message())

    def test_logging_first_number_is_empty(self):
        self.view_model.set_second_number("3/5")
        self.view_model.validate_input_numbers()
        self.assertEqual("First number is empty",
                         self.view_model.logger.get_last_message())

    def test_logging_first_number_is_invalid(self):
        self.view_model.set_first_number(r"3\5")
        self.view_model.set_second_number("3/5")
        self.view_model.validate_input_numbers()
        self.assertEqual("First number is invalid",
                         self.view_model.logger.get_last_message())

    def test_logging_first_numbers_denominator_is_null(self):
        self.view_model.set_first_number("3/0")
        self.view_model.set_second_number("3/5")
        self.view_model.validate_input_numbers()
        self.assertEqual("Denominator of first number is zero",
                         self.view_model.logger.get_last_message())

    def test_logging_second_number_is_empty(self):
        self.view_model.set_first_number("3/5")
        self.view_model.validate_input_numbers()
        self.assertEqual("Second number is empty",
                         self.view_model.logger.get_last_message())

    def test_logging_second_number_is_invalid(self):
        self.view_model.set_first_number("3/5")
        self.view_model.set_second_number(r"3\5")
        self.view_model.validate_input_numbers()
        self.assertEqual("Second number is invalid",
                         self.view_model.logger.get_last_message())

    def test_logging_second_numbers_denominator_is_null(self):
        self.view_model.set_first_number("3/5")
        self.view_model.set_second_number("3/0")
        self.view_model.validate_input_numbers()
        self.assertEqual("Denominator of second number is zero",
                         self.view_model.logger.get_last_message())

    def test_logging_operation_is_invalid(self):
        self.view_model.set_operation("//")
        self.view_model.validate_operation()
        self.assertEqual("Operation // is invalid",
                         self.view_model.logger.get_last_message())

    def test_division_by_zero(self):
        self.view_model.set_first_number("3/4")
        self.view_model.set_second_number("0/5")
        self.view_model.set_operation("/")
        self.view_model.validate_input()
        self.assertEqual("Division by zero",
                         self.view_model.logger.get_last_message())

    def test_numbers_and_operation_are_correct(self):
        self.view_model.set_first_number("3/4")
        self.view_model.set_second_number("3/5")
        self.view_model.set_operation("*")
        self.view_model.validate_input()
        self.assertEqual("Operation and input numbers are correct",
                         self.view_model.logger.get_last_message())

    def test_logger_calculate(self):
        self.view_model.set_first_number("3/4")
        self.view_model.set_second_number("3/5")
        self.view_model.set_operation("*")
        self.view_model.calculate()
        self.assertEqual("Calculating was finished successfully. Result: 3/4 * 3/5 = 9/20",
                         self.view_model.logger.get_last_message())


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = RationalNumberViewModel(RealLogger())
