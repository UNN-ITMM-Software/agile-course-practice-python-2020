import unittest

from viewmodel import StringFormulaCalculationViewModel
from infrastructure.fake_logger import FakeLogger
from infrastructure.real_logger import RealLogger


class TestNumberOperationsViewModel(unittest.TestCase):
    def setUp(self):
        self.model = StringFormulaCalculationViewModel()

    def test_warning_is_empty_by_default(self):
        self.assertEqual('', self.model.get_warning())

    def test_string_formula_setup_correct(self):
        self.model.set_formula('123')
        self.model.calculate_formula()
        self.assertEqual('123', self.model.get_formula())

    def test_calculating_invalid(self):
        self.model.set_formula('abc')
        self.model.calculate_formula()
        self.assertEqual('Invalid operation!', self.model.get_warning())

    def test_result_are_empty_by_default(self):
        self.assertEqual('', self.model.get_result())

    def test_calculation_adding_numbers(self):
        self.model.set_formula('5+5')
        self.model.calculate_formula()
        expected = 10.0
        self.assertEqual(expected, self.model.get_result())

    def test_calculation_subtracting_numbers(self):
        self.model.set_formula('255-10')
        self.model.calculate_formula()
        expected = 245.0
        self.assertEqual(expected, self.model.get_result())

    def test_multiplying_numbres(self):
        self.model.set_formula('10*10')
        self.model.calculate_formula()
        expected = 100.0
        self.assertEqual(expected, self.model.get_result())

    def test_dividing_numbers(self):
        self.model.set_formula('10/10')
        self.model.calculate_formula()
        expected = 1.0
        self.assertEqual(expected, self.model.get_result())

    def test_dividing_zero(self):
        self.model.set_formula('10 / 0')
        self.model.calculate_formula()
        self.assertEqual('Invalid operation!', self.model.get_warning())

    def test_adding_invalid_formula(self):
        self.model.set_formula('a+a')
        self.model.calculate_formula()
        self.assertEqual('Invalid operation!', self.model.get_warning())

    def test_subtracting_invalid_formula(self):
        self.model.set_formula('a-a')
        self.model.calculate_formula()
        self.assertEqual('Invalid operation!', self.model.get_warning())

    def test_multiplying_invalid_formula(self):
        self.model.set_formula('a*a')
        self.model.calculate_formula()
        self.assertEqual('Invalid operation!', self.model.get_warning())

    def test_dividing_invalid_formula(self):
        self.model.set_formula('a/a')
        self.model.calculate_formula()
        self.assertEqual('Invalid operation!', self.model.get_warning())


class TestNumberOperationsViewModelFakeLogger(unittest.TestCase):
    def setUp(self):
        self.model = StringFormulaCalculationViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual(['Start Logging'], self.model.logger.get_last_messages(1))

    def test_logging_setting_formula(self):
        formula = '10+2+1+1/1/4/7*90'
        self.model.set_formula(formula)
        self.assertEqual(['Setting formula sting: {}'.format(formula)],
                         self.model.logger.get_last_messages(1))

    def test_logging_formula_to_be_calculated(self):
        formula = '10+10'
        self.model.set_formula(formula)
        self.model.calculate_formula()
        logger_message = self.model.logger.get_last_messages(2)[0]
        self.assertEqual('Calculate: {}'.format(formula), logger_message)

    def test_logging_adding_result(self):
        self.model.set_formula('10+10')
        self.model.calculate_formula()
        self.assertEqual(['Calculation result: 20.0'],
                         self.model.logger.get_last_messages(1))

    def test_logging_subtracting_result(self):
        self.model.set_formula('20-10')
        self.model.calculate_formula()
        self.assertEqual(['Calculation result: 10.0'],
                         self.model.logger.get_last_messages(1))

    def test_logging_multiplying_result(self):
        self.model.set_formula('10*10')
        self.model.calculate_formula()
        self.assertEqual(['Calculation result: 100.0'],
                         self.model.logger.get_last_messages(1))

    def test_logging_dividing_result(self):
        self.model.set_formula('10/10')
        self.model.calculate_formula()
        self.assertEqual(['Calculation result: 1.0'],
                         self.model.logger.get_last_messages(1))


class TestNumberOperationsModelRealLogger(TestNumberOperationsViewModelFakeLogger):
    def setUp(self):
        self.model = StringFormulaCalculationViewModel(RealLogger())
