import unittest

from number_operations.viewmodel.viewmodel import NumberOperationsViewModel
from number_operations.infrastructure.fake_logger import FakeLogger
from number_operations.infrastructure.real_logger import RealLogger


class TestNumberOperationsViewModel(unittest.TestCase):
    def setUp(self):
        self.model = NumberOperationsViewModel()

    def test_warning_is_empty_by_default(self):
        self.assertEqual('', self.model.get_warning())

    def test_converting_first_decimal(self):
        self.model.set_first('123', '123', '123')
        self.model.convert_first_dec()
        self.assertEqual('123', self.model.get_first_dec())
        self.assertEqual('1111011', self.model.get_first_bin())
        self.assertEqual('7b', self.model.get_first_hex())

    def test_converting_first_binary(self):
        self.model.set_first('11', '1010', 'b')
        self.model.convert_first_bin()
        self.assertEqual('10', self.model.get_first_dec())
        self.assertEqual('1010', self.model.get_first_bin())
        self.assertEqual('a', self.model.get_first_hex())

    def test_converting_first_hexadecimal(self):
        self.model.set_first('abc', 'sdl', 'ff')
        self.model.convert_first_hex()
        self.assertEqual('255', self.model.get_first_dec())
        self.assertEqual('11111111', self.model.get_first_bin())
        self.assertEqual('ff', self.model.get_first_hex())

    def test_converting_second_decimal(self):
        self.model.set_second('123', '123', '123')
        self.model.convert_second_dec()
        self.assertEqual('123', self.model.get_second_dec())
        self.assertEqual('1111011', self.model.get_second_bin())
        self.assertEqual('7b', self.model.get_second_hex())

    def test_converting_second_binary(self):
        self.model.set_second('11', '1010', 'b')
        self.model.convert_second_bin()
        self.assertEqual('10', self.model.get_second_dec())
        self.assertEqual('1010', self.model.get_second_bin())
        self.assertEqual('a', self.model.get_second_hex())

    def test_converting_second_hexadecimal(self):
        self.model.set_second('abc', 'sdl', 'ff')
        self.model.convert_second_hex()
        self.assertEqual('255', self.model.get_second_dec())
        self.assertEqual('11111111', self.model.get_second_bin())
        self.assertEqual('ff', self.model.get_second_hex())

    def test_converting_invalid_first_dec(self):
        self.model.set_first('abc', 'abc', 'abc')
        self.model.convert_first_dec()
        self.assertEqual('Incorrect input!', self.model.get_warning())

    def test_converting_invalid_first_bin(self):
        self.model.set_first('abc', 'abc', 'abc')
        self.model.convert_first_bin()
        self.assertEqual('Incorrect input!', self.model.get_warning())

    def test_converting_invalid_first_hex(self):
        self.model.set_first('abc', 'abc', 'zzz')
        self.model.convert_first_hex()
        self.assertEqual('Incorrect input!', self.model.get_warning())

    def test_converting_invalid_second_dec(self):
        self.model.set_second('abc', 'abc', 'abc')
        self.model.convert_second_dec()
        self.assertEqual('Incorrect input!', self.model.get_warning())

    def test_converting_invalid_second_bin(self):
        self.model.set_second('abc', 'abc', 'abc')
        self.model.convert_second_bin()
        self.assertEqual('Incorrect input!', self.model.get_warning())

    def test_converting_invalid_second_hex(self):
        self.model.set_second('abc', 'abc', 'zzz')
        self.model.convert_second_hex()
        self.assertEqual('Incorrect input!', self.model.get_warning())

    def test_result_are_zeroes_by_default(self):
        self.assertEqual('0', self.model.get_result_dec())
        self.assertEqual('0', self.model.get_result_bin())
        self.assertEqual('0', self.model.get_result_hex())

    def test_adding_numbers(self):
        self.model.set_first('5', '0101', '5')
        self.model.set_second('10', '1010', 'a')
        self.model.convert_first_dec()
        self.model.convert_second_dec()
        self.model.add()
        self.assertEqual('15', self.model.get_result_dec())
        self.assertEqual('1111', self.model.get_result_bin())
        self.assertEqual('f', self.model.get_result_hex())

    def test_subtracting_numbers(self):
        self.model.set_first('255', '11111111', 'ff')
        self.model.set_second('10', '1010', 'a')
        self.model.convert_first_dec()
        self.model.convert_second_dec()
        self.model.subtract()
        self.assertEqual('245', self.model.get_result_dec())
        self.assertEqual('11110101', self.model.get_result_bin())
        self.assertEqual('f5', self.model.get_result_hex())

    def test_multiplying_numbres(self):
        self.model.set_first('10', '1010', 'a')
        self.model.set_second('5', '0101', '5')
        self.model.convert_first_dec()
        self.model.convert_second_dec()
        self.model.multiply()
        self.assertEqual('50', self.model.get_result_dec())
        self.assertEqual('110010', self.model.get_result_bin())
        self.assertEqual('32', self.model.get_result_hex())

    def test_dividing_numbers(self):
        self.model.set_first('10', '1010', 'a')
        self.model.set_second('5', '0101', '5')
        self.model.convert_first_dec()
        self.model.convert_second_dec()
        self.model.divide()
        self.assertEqual('2', self.model.get_result_dec())
        self.assertEqual('10', self.model.get_result_bin())
        self.assertEqual('2', self.model.get_result_hex())

    def test_dividing_zero(self):
        self.model.set_first('10', '1010', 'a')
        self.model.set_second('0', '0101', '5')
        self.model.convert_first_dec()
        self.model.convert_second_dec()
        self.model.divide()
        self.assertEqual('Invalid operation!', self.model.get_warning())

    def test_adding_invalid_numbers(self):
        self.model.set_first('a', '1010', 'a')
        self.model.set_second('b', '0101', '5')
        self.model.convert_first_dec()
        self.model.convert_second_dec()
        self.model.add()
        self.assertEqual('Invalid operation!', self.model.get_warning())

    def test_subtracting_invalid_numbers(self):
        self.model.set_first('a', '1010', 'a')
        self.model.set_second('b', '0101', '5')
        self.model.convert_first_dec()
        self.model.convert_second_dec()
        self.model.subtract()
        self.assertEqual('Invalid operation!', self.model.get_warning())

    def test_multiplying_invalid_numbers(self):
        self.model.set_first('a', '1010', 'a')
        self.model.set_second('b', '0101', '5')
        self.model.convert_first_dec()
        self.model.convert_second_dec()
        self.model.multiply()
        self.assertEqual('Invalid operation!', self.model.get_warning())


class TestNumberOperationsViewModelFakeLogger(unittest.TestCase):
    def setUp(self):
        self.model = NumberOperationsViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual(['Start Logging'], self.model.logger.get_last_messages(1))

    def test_logging_setting_first_number(self):
        self.model.set_first('10', '1010', 'a')
        self.assertEqual(['Setting first number: dec - 10, bin - 1010, hex - a'],
                         self.model.logger.get_last_messages(1))

    def test_logging_setting_second_number(self):
        self.model.set_second('10', '1010', 'a')
        self.assertEqual(['Setting second number: dec - 10, bin - 1010, hex - a'],
                         self.model.logger.get_last_messages(1))

    def test_logging_adding(self):
        self.model.set_first('10', '1010', 'a')
        self.model.set_second('10', '1010', 'a')
        self.model.add()
        self.assertEqual(['Adding 10 and 10'],
                         self.model.logger.get_last_messages(1))

    def test_logging_subtracting(self):
        self.model.set_first('10', '1010', 'a')
        self.model.set_second('10', '1010', 'a')
        self.model.subtract()
        self.assertEqual(['Subtracting 10 and 10'],
                         self.model.logger.get_last_messages(1))

    def test_logging_multiplying(self):
        self.model.set_first('10', '1010', 'a')
        self.model.set_second('10', '1010', 'a')
        self.model.multiply()
        self.assertEqual(['Multiplying 10 and 10'],
                         self.model.logger.get_last_messages(1))

    def test_logging_dividing(self):
        self.model.set_first('10', '1010', 'a')
        self.model.set_second('10', '1010', 'a')
        self.model.divide()
        self.assertEqual(['Dividing 10 and 10'],
                         self.model.logger.get_last_messages(1))

    def test_invalid_input(self):
        self.model.set_first('abc')
        self.model.convert_first_dec()
        self.assertEqual(['Incorrect input!'],
                         self.model.logger.get_last_messages(1))


class TestNumberOperationsModelRealLogger(TestNumberOperationsViewModelFakeLogger):
    def setUp(self):
        self.model = NumberOperationsViewModel(RealLogger())
