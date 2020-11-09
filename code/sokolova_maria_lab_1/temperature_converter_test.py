import unittest

from sokolova_maria_lab_1.temperature_converter import TemperatureConverter


class TemperatureConverterTest(unittest.TestCase):

    def test_can_create_converter(self):
        converter = TemperatureConverter(0)
        self.assertTrue(isinstance(converter, TemperatureConverter))

    def test_can_set_celsius_value_to_converter(self):
        celsius = 5
        self.assertEqual(celsius, TemperatureConverter(5).celsius)

    # Fahrenheit
    def test_convert_from_zero_f(self):
        zero_value = TemperatureConverter(0)
        self.assertAlmostEqual(zero_value.convert_to_fahrenheit(), 32)

    def test_convert_from_negative_value_f(self):
        negative_value = TemperatureConverter(-11)
        self.assertAlmostEqual(negative_value.convert_to_fahrenheit(), 12.2)

    def test_convert_from_positive_value_f(self):
        positive_value = TemperatureConverter(15)
        self.assertAlmostEqual(positive_value.convert_to_fahrenheit(), 59)

if __name__ == '__main__':
    unittest.main()
