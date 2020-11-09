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

    def test_convert_from_string_value_f(self):
        string_value = TemperatureConverter("-13")
        self.assertAlmostEqual(string_value.convert_to_fahrenheit(), 8.6)

    def test_convert_from_string_value_with_comma_f(self):
        string_value = TemperatureConverter("-13,5")
        self.assertAlmostEqual(string_value.convert_to_fahrenheit(), 7.7)

    def test_convert_from_string_value_with_point_f(self):
        string_value = TemperatureConverter("-13.5")
        self.assertAlmostEqual(string_value.convert_to_fahrenheit(), 7.7)

    # Kelvin
    def test_convert_from_zero_k(self):
        zero_value = TemperatureConverter(0)
        self.assertAlmostEqual(zero_value.convert_to_kelvin(), 273.15)

    def test_convert_from_negative_value_k(self):
        negative_value = TemperatureConverter(-11)
        self.assertAlmostEqual(negative_value.convert_to_kelvin(), 262.15)

    def test_convert_from_positive_value_k(self):
        positive_value = TemperatureConverter(15)
        self.assertAlmostEqual(positive_value.convert_to_kelvin(), 288.15)

    def test_convert_from_string_value_k(self):
        string_value = TemperatureConverter("-13")
        self.assertAlmostEqual(string_value.convert_to_kelvin(), 260.15)

    def test_convert_from_string_value_with_comma_k(self):
        string_value = TemperatureConverter("-13,5")
        self.assertAlmostEqual(string_value.convert_to_kelvin(), 259.65)

    def test_convert_from_string_value_with_point_k(self):
        string_value = TemperatureConverter("-13.5")
        self.assertAlmostEqual(string_value.convert_to_kelvin(), 259.65)

    # Newton
    def test_convert_from_zero_n(self):
        zero_value = TemperatureConverter(0)
        self.assertAlmostEqual(zero_value.convert_to_newton(), 0)

    def test_convert_from_negative_value_n(self):
        negative_value = TemperatureConverter(-11)
        self.assertAlmostEqual(negative_value.convert_to_newton(), -3.63)

    def test_convert_from_positive_value_n(self):
        positive_value = TemperatureConverter(15)
        self.assertAlmostEqual(positive_value.convert_to_newton(), 4.95)

    def test_convert_from_string_value_n(self):
        string_value = TemperatureConverter("-13")
        self.assertAlmostEqual(string_value.convert_to_newton(), -4.29)

    def test_convert_from_string_value_with_comma_n(self):
        string_value = TemperatureConverter("-13,5")
        self.assertAlmostEqual(string_value.convert_to_newton(), -4.455)

    def test_convert_from_string_value_with_point_n(self):
        string_value = TemperatureConverter("-13.5")
        self.assertAlmostEqual(string_value.convert_to_newton(), -4.455)


if __name__ == '__main__':
    unittest.main()
