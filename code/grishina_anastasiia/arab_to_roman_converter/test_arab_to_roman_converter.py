import unittest

from grishina_anastasiia.arab_to_roman_converter.arab_to_roman_converter import ArabToRomanConverter


class ArabToRomanConverterTest(unittest.TestCase):

    def test_class_creating(self):
        self.assertTrue(isinstance(ArabToRomanConverter(1), ArabToRomanConverter))

