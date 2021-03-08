from number_operations.model.number_converter import Converter


class Calculator():
    def __init__(self):
        self.first = 0
        self.second = 0
        self.result = 0

    def set_first(self, number, base):
        self.first = int(number, base)

    def set_second(self, number, base):
        self.second = int(number, base)

    def add(self, base):
        self.result = self.first + self.second
        return self.__result(base)

    def subtract(self, base):
        self.result = self.first - self.second
        return self.__result(base)

    def multiply(self, base):
        self.result = self.first * self.second
        return self.__result(base)

    def divide(self, base):
        self.result = self.first // self.second
        return self.__result(base)

    def __result(self, base):
        converter = Converter(str(self.result), 10)
        return converter.convert(base)
