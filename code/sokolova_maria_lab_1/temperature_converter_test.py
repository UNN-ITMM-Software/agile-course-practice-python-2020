import unittest

from sokolova_maria_lab_1.temperature_converter import TemperatureConverter


class TemperatureConverterTest(unittest.TestCase):

    def test_can_create_converter(self):
        converter = TemperatureConverter(0)
        self.assertTrue(isinstance(converter, TemperatureConverter))

    def test_can_set_celsius_value_to_converter(self):
        celsius = 5
        self.assertEqual(celsius, TemperatureConverter(5).celsius)


if __name__ == '__main__':
    unittest.main()
