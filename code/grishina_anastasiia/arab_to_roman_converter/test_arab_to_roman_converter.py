import unittest

from grishina_anastasiia.arab_to_roman_converter.arab_to_roman_converter import ArabToRomanConverter


class ArabToRomanConverterTest(unittest.TestCase):

    def test_class_creating(self):
        self.assertTrue(isinstance(ArabToRomanConverter(1), ArabToRomanConverter))

    def test_convert_arab_one_to_roman(self):
        converter = ArabToRomanConverter(1)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'I')

    def test_convert_arab_five_to_roman(self):
        converter = ArabToRomanConverter(2)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'II')
