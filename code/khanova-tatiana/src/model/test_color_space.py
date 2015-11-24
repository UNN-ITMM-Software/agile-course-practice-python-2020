import unittest
import numpy as np
from color_space import ColorSpace, InvalidColorSpace
from color import Color, InvalidColorError
from color_space_converter import ColorSpaceConverter, InvalidConversion


class TestColorSpaceClass(unittest.TestCase):
    def test_can_create_empty_color_space(self):
        color_space = ColorSpace()
        self.assertTrue(isinstance(color_space, ColorSpace))

    def test_can_create_default_rgb_color_space(self):
        color_space = ColorSpace()
        self.assertEqual(str(color_space), "RGB")

    def test_cannot_create_invalid_color_space(self):
        with self.assertRaises(InvalidColorSpace):
            ColorSpace("QQQ")

    def test_cannot_create_invalid_color_space_type(self):
        with self.assertRaises(InvalidColorSpace):
            ColorSpace(1)


class TestColorClass(unittest.TestCase):
    def test_can_create_empty_color(self):
        color = Color()
        self.assertTrue(isinstance(color, Color))

    def test_can_create_default_rgb_color(self):
        color = Color()
        self.assertEqual(str(color), "RGB [0, 0, 0]")

    def test_can_create_default_hsv_color(self):
        color = Color(ColorSpace("HSV"))
        self.assertEqual(str(color), "HSV [0, 0, 0]")

    def test_can_create_default_lab_color(self):
        color = Color(ColorSpace("LAB"))
        self.assertEqual(str(color), "LAB [0, 0, 0]")

    def test_can_create_rgb_color(self):
        color = Color(ColorSpace("RGB"), np.array([123, 45, 67]))
        self.assertEqual(str(color), "{} {}".format("RGB",
                                                    np.array([123, 45,
                                                              67]).tolist()))

    def test_cannot_create_invalid_rgb_color_len(self):
        rand_color = np.random.randint(0, 255, size=(1, 10))
        with self.assertRaises(InvalidColorError):
            Color("RGB", rand_color)

    def test_cannot_create_invalid_rgb_color_val(self):
        rand_color = np.random.randint(300, 400, size=(1, Color.COLOR_DIM))
        with self.assertRaises(InvalidColorError):
            Color(ColorSpace("RGB"), rand_color)

    def test_cannot_create_invalid_rgb_color_val_neg(self):
        rand_color = np.random.randint(-100, -10, size=(1, Color.COLOR_DIM))
        with self.assertRaises(InvalidColorError):
            Color(ColorSpace("RGB"), rand_color)


class TestColorSpaceConverterClass(unittest.TestCase):
    def setUp(self):
        self.converter = ColorSpaceConverter()

    def test_can_create_color_space_converter(self):
        self.assertTrue(isinstance(self.converter, ColorSpaceConverter))

    def test_can_convert_rgb_to_rgb(self):
        color = Color()
        rgb_color = self.converter.convert(color, ColorSpace("RGB"))
        self.assertEqual(color, rgb_color)

    def test_can_convert_black_rgb_to_hsv(self):
        color = Color()
        hsv_color = self.converter.convert(color, ColorSpace("HSV"))
        self.assertEqual(hsv_color, Color(ColorSpace("HSV")))

    def test_can_convert_simple_rgb_to_hsv(self):
        color = Color(ColorSpace("RGB"), np.array([0, 100, 0]))
        hsv_color = self.converter.convert(color, ColorSpace("HSV"))
        self.assertEquals(hsv_color, Color(ColorSpace("HSV"),
                                           np.array([85, 255, 100])))

    def test_can_convert_rgb_to_hsv(self):
        color = Color(ColorSpace("RGB"), np.array([91, 71, 123]))
        hsv_color = self.converter.convert(color, ColorSpace("HSV"))
        self.assertEquals(hsv_color, Color(ColorSpace("HSV"),
                                           np.array([186, 108, 123])))

    def test_can_convert_rgb_to_hsv_1(self):
        color = Color(ColorSpace("RGB"), np.array([191, 71, 123]))
        hsv_color = self.converter.convert(color, ColorSpace("HSV"))
        self.assertEquals(hsv_color, Color(ColorSpace("HSV"),
                                           np.array([237, 160, 191])))

    def test_can_convert_black_hsv_to_rgb(self):
        color = Color(ColorSpace("HSV"))
        rgb_color = self.converter.convert(color, ColorSpace("RGB"))
        self.assertEqual(rgb_color, Color(ColorSpace("RGB")))

    def test_can_convert_simple_hsv_to_rgb(self):
        color = Color(ColorSpace("HSV"), np.array([0, 100, 0]))
        rgb_color = self.converter.convert(color, ColorSpace("RGB"))
        self.assertEqual(rgb_color, Color(ColorSpace("RGB"),
                                          np.array([0, 0, 0])))

    def test_can_convert_hsv_to_rgb_2(self):
        color = Color(ColorSpace("HSV"), np.array([56, 108, 123]))
        rgb_color = self.converter.convert(color, ColorSpace("RGB"))
        self.assertEqual(rgb_color, Color(ColorSpace("RGB"),
                                          np.array([106, 123, 71])))

    def test_can_convert_hsv_to_rgb_3(self):
        color = Color(ColorSpace("HSV"), np.array([114, 108, 123]))
        rgb_color = self.converter.convert(color, ColorSpace("RGB"))
        self.assertEqual(rgb_color, Color(ColorSpace("RGB"),
                                          np.array([71, 123, 106])))

    def test_can_convert_hsv_to_rgb_4(self):
        color = Color(ColorSpace("HSV"), np.array([142, 50, 60]))
        rgb_color = self.converter.convert(color, ColorSpace("RGB"))
        self.assertEqual(rgb_color, Color(ColorSpace("RGB"),
                                          np.array([48, 56, 60])))

    def test_can_convert_hsv_to_rgb_5(self):
        color = Color(ColorSpace("HSV"), np.array([187, 108, 123]))
        rgb_color = self.converter.convert(color, ColorSpace("RGB"))
        self.assertEqual(rgb_color, Color(ColorSpace("RGB"),
                                          np.array([92, 71, 123])))

    def test_can_convert_hsv_to_rgb_6(self):
        color = Color(ColorSpace("HSV"), np.array([247, 108, 123]))
        rgb_color = self.converter.convert(color, ColorSpace("RGB"))
        self.assertEqual(rgb_color, Color(ColorSpace("RGB"),
                                          np.array([123, 71, 81])))

    def test_can_convert_black_rgb_to_lab(self):
        color = Color()
        lab_color = self.converter.convert(color, ColorSpace("LAB"))
        self.assertEqual(lab_color, Color(ColorSpace("LAB"),
                                          np.array([0, 128, 128])))

    def test_can_convert_simple_rgb_to_lab(self):
        color = Color(ColorSpace("RGB"), np.array([0, 100, 0]))
        lab_color = self.converter.convert(color, ColorSpace("LAB"))
        self.assertEqual(lab_color, Color(ColorSpace("LAB"),
                                          np.array([92, 85, 170])))

    def test_can_convert_rgb_to_lab(self):
        color = Color(ColorSpace("RGB"), np.array([91, 71, 123]))
        lab_color = self.converter.convert(color, ColorSpace("LAB"))
        self.assertEqual(lab_color, Color(ColorSpace("LAB"),
                                          np.array([88, 148, 101])))

    def test_can_convert_lab_to_rgb(self):
        color = Color(ColorSpace("LAB"), np.array([88, 148, 101]))
        rgb_color = self.converter.convert(color, ColorSpace("RGB"))
        self.assertEqual(rgb_color, Color(ColorSpace("RGB"),
                                          np.array([90, 72, 124])))

    def test_can_convert_lab_to_rgb_1(self):
        color = Color(ColorSpace("LAB"), np.array([80, 79, 185]))
        rgb_color = self.converter.convert(color, ColorSpace("RGB"))
        self.assertEqual(rgb_color, Color(ColorSpace("RGB"),
                                          np.array([0, 89, 0])))

    def test_cannot_create_unimplemented_converter(self):
        color = Color(ColorSpace("HSV"))
        with self.assertRaises(InvalidConversion):
            self.converter.convert(color, ColorSpace("LAB"))
