import unittest

from length_converter.model.length_converter import LengthConverter


class TemperatureConverterTest(unittest.TestCase):
    def test_can_create_converter(self):
        converter = LengthConverter(0, 0)
        self.assertTrue(isinstance(converter, LengthConverter))
