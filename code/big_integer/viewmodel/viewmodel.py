import re
from enum import Enum

import numpy as np

from big_integer.model.big_integer import BigInteger


class Operation(Enum):
    ADDITIONAL = 0
    SUBTRACTION = 1
    MULTIPLICATION = 2


class CalculateState(Enum):
    ENABLE = 0
    DISABLE = 1


def string_to_big_integer(string):
    np_array = np.array([])
    for i, v in enumerate(string):
        np_array = np.insert(np_array, 0, int(v))
    return BigInteger(np_array.tolist())


def big_integer_to_string(big_integer):
    string = ''
    tmp = False
    for i in reversed(range(big_integer.SIZE)):
        if tmp:
            string += str(int(big_integer.digits[i]))
        elif big_integer.digits[i] != 0:
            string += str(int(big_integer.digits[i]))
            tmp = True
    if string == '':
        string = '0'
    return string


def is_valid(string):
    return string is not None and string != "" and re.compile("^\d*$").match(string) is not None


class BigIntegerViewModel:
    def __init__(self):
        self.a = "456"
        self.b = "123"
        self.operation = Operation.ADDITIONAL
        self.result = "579"
        self.calculate_state = CalculateState.ENABLE

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_operation(self):
        return self.operation

    def get_calculate_state(self):
        return self.calculate_state

    def get_result(self):
        return self.result

    def set_a(self, a):
        self.a = a
        if is_valid(self.a) and is_valid(self.b):
            self.calculate_state = CalculateState.ENABLE
        else:
            self.calculate_state = CalculateState.DISABLE

    def set_b(self, b):
        self.b = b
        if is_valid(self.a) and is_valid(self.b):
            self.calculate_state = CalculateState.ENABLE
        else:
            self.calculate_state = CalculateState.DISABLE

    def set_operation(self, operation):
        self.operation = operation

    def calculate(self):
        big_a = string_to_big_integer(self.a)
        big_b = string_to_big_integer(self.b)
        if self.operation == Operation.ADDITIONAL:
            self.result = big_integer_to_string(big_a + big_b)
        elif self.operation == Operation.SUBTRACTION:
            self.result = big_integer_to_string(big_a - big_b)
        elif self.operation == Operation.MULTIPLICATION:
            self.result = big_integer_to_string(big_a * big_b)
        self.calculate_state = CalculateState.ENABLE
