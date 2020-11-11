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

    def test_can_convert_1000_meter_to_meter(self):
        converter = LengthConverter(1000, LengthType.meter)
        meter = converter.convert(LengthType.meter)
        self.assertEqual(meter, 1000)

    def test_can_convert_10_meter_to_centimeter(self):
        converter = LengthConverter(10, LengthType.meter)
        cm = converter.convert(LengthType.centimeter)
        self.assertEqual(cm, 10*100)

    def test_can_convert_100_centimeter_to_meter(self):
        converter = LengthConverter(100, LengthType.centimeter)
        meter = converter.convert(LengthType.meter)
        self.assertEqual(meter, 1)

    def test_can_create_negative_converter(self):
        with self.assertRaises(ValueError):
            LengthConverter(-1.0, LengthType.meter)

    def test_can_create_converter_from_string(self):
        converter = LengthConverter("1.0", LengthType.meter)
        self.assertTrue(isinstance(converter, LengthConverter))

    def test_can_convert_10_meter_to_centimeter_from_string(self):
        converter = LengthConverter("10.0", LengthType.meter)
        cm = converter.convert(LengthType.centimeter)
        self.assertEqual(cm, 10*100)

    def test_can_convert_1_meter_to_millimeter(self):
        converter = LengthConverter(1, LengthType.meter)
        mm = converter.convert(LengthType.millimeter)
        self.assertEqual(mm, 1*1000)

    def test_can_convert_1000_millimeter_to_meter(self):
        converter = LengthConverter(1000, LengthType.millimeter)
        m = converter.convert(LengthType.meter)
        self.assertEqual(m, 1)

    def test_can_convert_1000_meter_to_kilometer(self):
        converter = LengthConverter(1000, LengthType.meter)
        km = converter.convert(LengthType.kilometer)
        self.assertEqual(km, 1)

    def test_can_convert_1_kilometer_to_meter(self):
        converter = LengthConverter(1, LengthType.kilometer)
        m = converter.convert(LengthType.meter)
        self.assertEqual(m, 1000)
