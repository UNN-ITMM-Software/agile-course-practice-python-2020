import unittest

from length_converter.model.length_converter import LengthConverter, LengthType


class TemperatureConverterTest(unittest.TestCase):
    def test_can_create_converter(self):
        converter = LengthConverter(0.0, LengthType.meter)
        self.assertTrue(isinstance(converter, LengthConverter))

    def test_can_convert_zero_meter_to_meter(self):
        converter = LengthConverter(0.0, LengthType.meter)
        meter = converter.convert(LengthType.meter)
        self.assertAlmostEqual(meter, 0)

    def test_can_convert_1000_meter_to_meter(self):
        converter = LengthConverter(1000.0, LengthType.meter)
        meter = converter.convert(LengthType.meter)
        self.assertAlmostEqual(meter, 1000.0)

    def test_can_convert_10_meter_to_centimeter(self):
        converter = LengthConverter(10.0, LengthType.meter)
        cm = converter.convert(LengthType.centimeter)
        self.assertAlmostEqual(cm, 10.0*100.0)

    def test_can_convert_100_centimeter_to_meter(self):
        converter = LengthConverter(100.0, LengthType.centimeter)
        meter = converter.convert(LengthType.meter)
        self.assertAlmostEqual(meter, 1.0)

    def test_can_create_negative_converter(self):
        with self.assertRaises(ValueError):
            LengthConverter(-1.0, LengthType.meter)

    def test_can_create_converter_from_string(self):
        converter = LengthConverter("1.0", LengthType.meter)
        self.assertTrue(isinstance(converter, LengthConverter))

    def test_can_convert_10_meter_to_centimeter_from_string(self):
        converter = LengthConverter("10.0", LengthType.meter)
        cm = converter.convert(LengthType.centimeter)
        self.assertAlmostEqual(cm, 10.0*100.0)

    def test_can_convert_1_meter_to_millimeter(self):
        converter = LengthConverter(1.0, LengthType.meter)
        mm = converter.convert(LengthType.millimeter)
        self.assertAlmostEqual(mm, 1.0*1000.0)

    def test_can_convert_1000_millimeter_to_meter(self):
        converter = LengthConverter(1000.0, LengthType.millimeter)
        m = converter.convert(LengthType.meter)
        self.assertAlmostEqual(m, 1.0)

    def test_can_convert_1000_meter_to_kilometer(self):
        converter = LengthConverter(1000.0, LengthType.meter)
        km = converter.convert(LengthType.kilometer)
        self.assertAlmostEqual(km, 1.0)

    def test_can_convert_1_kilometer_to_meter(self):
        converter = LengthConverter(1.0, LengthType.kilometer)
        m = converter.convert(LengthType.meter)
        self.assertAlmostEqual(m, 1000.0)

    def test_can_convert_1000000_centimeter_to_mile(self):
        converter = LengthConverter(1000000.0, LengthType.centimeter)
        mile = converter.convert(LengthType.mile)
        self.assertAlmostEqual(mile, 6.2137)

    def test_can_convert_1_mile_to_meter(self):
        converter = LengthConverter(6.2137, LengthType.mile)
        m = converter.convert(LengthType.meter)
        self.assertAlmostEqual(m, 10000.0)

