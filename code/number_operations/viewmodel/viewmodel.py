from number_operations.model.number_calculator import Calculator
from number_operations.model.number_converter import Converter
from number_operations.infrastructure.real_logger import RealLogger


class NumberOperationsViewModel:
    def __init__(self, logger=RealLogger()):
        self.calculator = Calculator()
        self.first_dec = self.second_dec = self.result_dec = '0'
        self.first_bin = self.second_bin = self.result_bin = '0'
        self.first_hex = self.second_hex = self.result_hex = '0'
        self.warning = ''
        self.logger = logger
        self.logger.log('Start Logging')

    def set_first(self, decimal='0', binary='0', hexadecimal='0'):
        self.logger.log('Setting first number: dec - {}, bin - {}, hex - {}'.
                        format(decimal, binary, hexadecimal))
        self.first_dec = decimal
        self.first_bin = binary
        self.first_hex = hexadecimal

    def set_second(self, decimal='0', binary='0', hexadecimal='0'):
        self.logger.log('Setting second number: dec - {}, bin - {}, hex - {}'.
                        format(decimal, binary, hexadecimal))
        self.second_dec = decimal
        self.second_bin = binary
        self.second_hex = hexadecimal

    def convert_first_dec(self):
        self.warning = ''
        try:
            converter = Converter(self.first_dec, 10)
            self.first_bin = converter.convert(2)
            self.first_hex = converter.convert(16)
        except:
            self.logger.log('Incorrect input!')
            self.warning = 'Incorrect input!'

    def convert_first_bin(self):
        self.warning = ''
        try:
            converter = Converter(self.first_bin, 2)
            self.first_dec = converter.convert(10)
            self.first_hex = converter.convert(16)
        except:
            self.logger.log('Incorrect input!')
            self.warning = 'Incorrect input!'

    def convert_first_hex(self):
        self.warning = ''
        try:
            converter = Converter(self.first_hex, 16)
            self.first_dec = converter.convert(10)
            self.first_bin = converter.convert(2)
        except:
            self.logger.log('Incorrect input!')
            self.warning = 'Incorrect input!'

    def convert_second_dec(self):
        self.warning = ''
        try:
            converter = Converter(self.second_dec, 10)
            self.second_bin = converter.convert(2)
            self.second_hex = converter.convert(16)
        except:
            self.logger.log('Incorrect input!')
            self.warning = 'Incorrect input!'

    def convert_second_bin(self):
        self.warning = ''
        try:
            converter = Converter(self.second_bin, 2)
            self.second_dec = converter.convert(10)
            self.second_hex = converter.convert(16)
        except:
            self.logger.log('Incorrect input!')
            self.warning = 'Incorrect input!'

    def convert_second_hex(self):
        self.warning = ''
        try:
            converter = Converter(self.second_hex, 16)
            self.second_dec = converter.convert(10)
            self.second_bin = converter.convert(2)
        except:
            self.logger.log('Incorrect input!')
            self.warning = 'Incorrect input!'

    def add(self):
        self.warning = ''
        self.logger.log('Adding {} and {}'.
                        format(self.first_dec, self.second_dec))
        try:
            self.calculator.set_first(self.first_dec, 10)
            self.calculator.set_second(self.second_dec, 10)
            self.result_dec = self.calculator.add(10)
            self.result_bin = self.calculator.add(2)
            self.result_hex = self.calculator.add(16)
        except:
            self.warning = 'Invalid operation!'

    def subtract(self):
        self.warning = ''
        self.logger.log('Subtracting {} and {}'.
                        format(self.first_dec, self.second_dec))
        try:
            self.calculator.set_first(self.first_dec, 10)
            self.calculator.set_second(self.second_dec, 10)
            self.result_dec = self.calculator.subtract(10)
            self.result_bin = self.calculator.subtract(2)
            self.result_hex = self.calculator.subtract(16)
        except:
            self.warning = 'Invalid operation!'

    def multiply(self):
        self.logger.log('Multiplying {} and {}'.
                        format(self.first_dec, self.second_dec))
        self.warning = ''
        try:
            self.calculator.set_first(self.first_dec, 10)
            self.calculator.set_second(self.second_dec, 10)
            self.result_dec = self.calculator.multiply(10)
            self.result_bin = self.calculator.multiply(2)
            self.result_hex = self.calculator.multiply(16)
        except:
            self.warning = 'Invalid operation!'

    def divide(self):
        self.logger.log('Dividing {} and {}'.
                        format(self.first_dec, self.second_dec))
        self.warning = ''
        try:
            self.calculator.set_first(self.first_dec, 10)
            self.calculator.set_second(self.second_dec, 10)
            self.result_dec = self.calculator.divide(10)
            self.result_bin = self.calculator.divide(2)
            self.result_hex = self.calculator.divide(16)
        except:
            self.warning = 'Invalid operation!'

    def get_first_dec(self):
        return self.first_dec

    def get_first_bin(self):
        return self.first_bin

    def get_first_hex(self):
        return self.first_hex

    def get_second_dec(self):
        return self.second_dec

    def get_second_bin(self):
        return self.second_bin

    def get_second_hex(self):
        return self.second_hex

    def get_result_dec(self):
        return self.result_dec

    def get_result_bin(self):
        return self.result_bin

    def get_result_hex(self):
        return self.result_hex

    def get_warning(self):
        return self.warning
