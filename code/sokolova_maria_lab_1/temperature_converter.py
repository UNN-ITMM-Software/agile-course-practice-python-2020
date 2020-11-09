import math


class TemperatureConverter:

    def __init__(self, celsius):
        if isinstance(celsius, str):
            celsius = celsius.replace(',', '.')
        self.celsius = float(celsius)

    def convert_to_fahrenheit(self):
        return float((self.celsius * 1.8)) + 32

    def convert_to_kelvin(self):
        return float(self.celsius + 273.15)
    
    def convert_to_newton(self):
        return float(self.celsius * 0.33)
