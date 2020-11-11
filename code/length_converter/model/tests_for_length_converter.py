import unittest

from length_converter.model.length_converter import LengthConverter, LengthType


class TemperatureConverterTest(unittest.TestCase):
    def test_can_create_converter(self):
        converter = LengthConverter(0, LengthType.meter)
        self.assertTrue(isinstance(converter, LengthConverter))

    def test_can_convert_zero_meter_to_meter(self):
        converter = LengthConverter(0, LengthType.meter)
        meter = converter.convert(LengthType.meter)
        self.assertEqual(meter, 0)
