import math


class TemperatureConverter:

    def __init__(self, celsius):
        self.celsius = celsius

    def convert_to_fahrenheit(self):
        return float((self.celsius * 1.8)) + 32
