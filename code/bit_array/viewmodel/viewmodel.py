from bit_array.model.bit_array import BitArray
from bit_array.viewmodel.operation import Operation
import re

from bit_array.logger.reallogger import RealLogger


class BitArrayViewModel:
    def __init__(self, logger=RealLogger()):
        self.__left_bit_array = None
        self.__right_bit_array = None
        self.__operation = Operation.OR
        self.__result = None
        self.__left_bit_array_enabled = True
        self.logger = logger
        self.logger.log('Welcome!')

    def calculate(self):
        if self.__operation == Operation.OR:
            self.__set_result(self.__left_bit_array | self.__right_bit_array)
        if self.__operation == Operation.AND:
            self.__set_result(self.__left_bit_array & self.__right_bit_array)
        if self.__operation == Operation.XOR:
            self.__set_result(self.__left_bit_array ^ self.__right_bit_array)
        if self.__operation == Operation.EQ:
            self.__set_result(self.__left_bit_array == self.__right_bit_array)
        if self.__operation == Operation.NEQ:
            self.__set_result(self.__left_bit_array != self.__right_bit_array)
        if self.__operation == Operation.INVERT:
            self.__set_result(~ self.__right_bit_array)

    def __set_result(self, value):
        self.__result = value
        if isinstance(self.__result, bool):
            if self.__result:
                res_log = 'YES'
            else:
                res_log = 'NO'
        else:
            res_log = self.__result.to_string()

        self.logger.log('Set result with {}'.format(res_log))

    def get_result(self):
        return self.__result

    def clear_result(self):
        self.logger.log('Clear previous result')
        self.__result = None

    def get_result_string(self):
        if self.__result is None:
            return ''
        if isinstance(self.__result, bool):
            return 'YES' if self.__result else 'NO'
        return self.__result.to_string()[-self.__result.get_length():]

    def set_left_bit_array(self, left_bit_array):
        self.__left_bit_array = self.bit_array_from_string(left_bit_array)
        self.logger.log('Set left bit array with {}'.format(self.__left_bit_array.to_string()))

    def get_left_bit_array_string(self):
        if self.__left_bit_array is None:
            return ''
        return self.__left_bit_array.to_string()[-self.__left_bit_array.get_length():]

    def get_right_bit_array_string(self):
        if self.__right_bit_array is None:
            return ''
        return self.__right_bit_array.to_string()[-self.__right_bit_array.get_length():]

    def set_right_bit_array(self, right_bit_array):
        self.__right_bit_array = self.bit_array_from_string(right_bit_array)
        self.logger.log('Set right bit array with {}'.format(self.__right_bit_array.to_string()))

    def set_operation(self, operation):
        self.__operation = operation
        self.__left_bit_array_enabled = operation != Operation.INVERT
        self.logger.log('Set operation with {}'.format(self.__operation))
        if not self.__left_bit_array_enabled:
            self.logger.log('Disable left bit array')

    def get_operation(self):
        return self.__operation

    def get_left_bit_array_enabled(self):
        return self.__left_bit_array_enabled

    def bit_array_from_string(self, string):
        if not re.fullmatch('[0|1]+', string):
            self.logger.log('Error:\n     '
                            'Can\'t convert "{}" '
                            'to bit array'.format(string))
            raise ValueError('Wrong format of bit array.')
        bit_array = BitArray(len(string))
        reversed_string = string[::-1]
        for bit_index in range(0, len(string), 1):
            if reversed_string[bit_index] == '1':
                bit_array.set_bit(bit_index)
        return bit_array
