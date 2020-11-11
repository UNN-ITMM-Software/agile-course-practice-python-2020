import unittest

from grishina_anastasiia.arab_to_roman_converter.arab_to_roman_converter import ArabToRomanConverter


class ArabToRomanConverterTest(unittest.TestCase):

    def test_class_creating(self):
        self.assertTrue(isinstance(ArabToRomanConverter(1), ArabToRomanConverter))

    def test_convert_arab_one_to_roman(self):
        converter = ArabToRomanConverter(1)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'I')

    def test_convert_arab_two_to_roman(self):
        converter = ArabToRomanConverter(2)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'II')

    def test_convert_arab_five_to_roman(self):
        converter = ArabToRomanConverter(5)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'V')

    def test_convert_arab_ten_to_roman(self):
        converter = ArabToRomanConverter(10)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'X')

    def test_convert_arab_seventy_to_roman(self):
        converter = ArabToRomanConverter(70)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'LXX')

    def test_convert_arab_fifteen_to_roman(self):
        converter = ArabToRomanConverter(15)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'XV')

    def test_convert_arab_eighty_two_to_roman(self):
        converter = ArabToRomanConverter(82)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'LXXXII')

    def test_convert_arab_hundred_to_roman(self):
        converter = ArabToRomanConverter(100)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'C')

    def test_convert_arab_150_to_roman(self):
        converter = ArabToRomanConverter(150)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'CL')

    def test_convert_arab_288_to_roman(self):
        converter = ArabToRomanConverter(288)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'CCLXXXVIII')

    def test_convert_arab_1000_to_roman(self):
        converter = ArabToRomanConverter(1000)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'M')
