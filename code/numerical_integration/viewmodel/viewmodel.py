import os

from enum import Enum
from numerical_integration.model.numerical_integration import NumericalIntegrator
from numerical_integration.logger.reallogger import RealLogger


class Operation(Enum):
    TRAPEZIUM_METHOD = 0
    SIMPSON_METHOD = 1


class CalculateState(Enum):
    ENABLE = 0
    DISABLE = 1


def is_valid(string):
    try:
        float(string)
        return True
    except Exception:
        return False


class NumericalIntegratorViewModel:
    def __init__(self,
                 logger=RealLogger(os.path.join('..', '..', 'tmp', 'numerical_integration.log'))):
        self.logger = logger
        self.logger.log('Hello')
        self.a = "0"
        self.b = "1"
        self.operation = Operation.TRAPEZIUM_METHOD
        self.result = "0.5"
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
        self.logger.log('Input a: {}'.format(a))
        self.a = a
        if is_valid(self.a) and is_valid(self.b):
            self.logger.log('Correct input a')
            self.calculate_state = CalculateState.ENABLE
        else:
            self.logger.log('Invalid input a')
            self.calculate_state = CalculateState.DISABLE

    def set_b(self, b):
        self.logger.log('Input b: {}'.format(b))
        self.b = b
        if is_valid(self.a) and is_valid(self.b):
            self.logger.log('Correct input b')
            self.calculate_state = CalculateState.ENABLE
        else:
            self.logger.log('Invalid input b')
            self.calculate_state = CalculateState.DISABLE

    def set_operation(self, operation):
        self.logger.log('Set operation: {}'.format(operation))
        self.operation = operation

    def calculate(self):
        self.logger.log('Button clicked')
        self.logger.log('Operation: {}'.format(self.operation))
        float_a = float(self.a)
        float_b = float(self.b)

        def func(x):
            return x

        if self.operation == Operation.TRAPEZIUM_METHOD:
            self.result = str(round(NumericalIntegrator().trapezium_method(float_a, float_b, func), 5))
        elif self.operation == Operation.SIMPSON_METHOD:
            self.result = str(round(NumericalIntegrator().simpson_method(float_a, float_b, func), 5))
        self.calculate_state = CalculateState.ENABLE
        self.logger.log('Result: {}'.format(self.result))
