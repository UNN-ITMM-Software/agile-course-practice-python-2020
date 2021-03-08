import unittest

from number_operations.model.number_converter import Converter


class TestNumberConverter(unittest.TestCase):
    def test_create_converter(self):
        converter = Converter('10', 2)
        self.assertTrue(isinstance(converter, Converter))

    def test_digit_outside_base(self):
        with self.assertRaises(ValueError):
            Converter('20', 2)

    def test_binary_to_decimal_conversion(self):
        converter = Converter('1010', 2)
        decimal = '10'
        self.assertEqual(decimal, converter.convert(10))

    def test_decimal_to_binary_conversion(self):
        converter = Converter('10', 10)
        binary = '1010'
        self.assertEqual(binary, converter.convert(2))

    def test_hex_to_decimal_conversion(self):
        converter = Converter('deadbeef', 16)
        decimal = '3735928559'
        self.assertEqual(decimal, converter.convert(10))

    def test_decimal_to_hex_conversion(self):
        converter = Converter('3735928559', 10)
        hex = 'deadbeef'
        self.assertEqual(hex, converter.convert(16))

    def test_decimal_to_oct_conversion(self):
        converter = Converter('10', 10)
        oct = '12'
        self.assertEqual(oct, converter.convert(8))

    def test_invalid_string(self):
        with self.assertRaises(ValueError):
            Converter('-^&#@', 2)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            Converter('-10', 10)
