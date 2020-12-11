import re
from enum import Enum

import numpy as np

from numerical_integration.model.numerical_integration import NumericalIntegrator


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
    def __init__(self):
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
        float_a = float(self.a)
        float_b = float(self.b)

        def func(x):
            return x

        if self.operation == Operation.TRAPEZIUM_METHOD:
            self.result = str(round(NumericalIntegrator().trapezium_method(float_a, float_b, func), 5))
        elif self.operation == Operation.SIMPSON_METHOD:
            self.result = str(round(NumericalIntegrator().simpson_method(float_a, float_b, func), 5))
        self.calculate_state = CalculateState.ENABLE
