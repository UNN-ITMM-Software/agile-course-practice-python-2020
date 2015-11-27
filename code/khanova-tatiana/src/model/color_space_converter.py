import numpy as np
from numpy.linalg import inv
import math
from color import Color
from color_space import ColorSpace
import utility


class InvalidConversion(Exception):
    pass


class ColorSpaceConverter:
    RGB2XYZ_CONVERSION_MAT = np.array([[0.412453, 0.357580, 0.180423],
                                       [0.212671, 0.715160, 0.072169],
                                       [0.019334, 0.119193, 0.950227]])

    WHITE_POINT = np.array([95.047, 100., 108.883])

    @staticmethod
    def rgb2hsv(self, color):
        color.value = color.value / 255.
        red, green, blue = color.value.tolist()

        max_val = max(color.value)
        min_val = min(color.value)
        diff = max_val - min_val

        if diff == 0:
            hue = 0
        elif max_val == red:
            hue = (green - blue) / diff
        elif max_val == green:
            hue = (blue - red) / diff + 2
        elif max_val == blue:
            hue = (red - green) / diff + 4

        hue *= 60
        hue = hue + 360 if hue < 0 else hue

        saturation = 0 if max_val == 0 else diff / max_val * 255
        value = max_val * 255
        hue *= 255. / 360.

        return Color(ColorSpace("HSV"),
                     np.round(np.array([hue, saturation, value])).astype(np.uint8))

    @staticmethod
    def hsv2rgb(self, color):
        hue = color.value[0] * 360. / 255. / 360. * 6
        saturation = color.value[1] / 255.
        value = color.value[2] / 255.

        chroma = value * saturation
        x = chroma * (1 - math.fabs(hue % 2 - 1))
        rgb = [0] * Color.COLOR_DIM
        hue = hue % 6

        if 0. <= hue < 1.:
            rgb = [chroma, x, 0]
        if 1. <= hue < 2.:
            rgb = [x, chroma, 0]
        if 2. <= hue < 3.:
            rgb = [0, chroma, x]
        if 3. <= hue < 4.:
            rgb = [0, x, chroma]
        if 4. <= hue < 5.:
            rgb = [x, 0, chroma]
        if 5. <= hue < 6.:
            rgb = [chroma, 0, x]

        min_val = value - chroma

        return Color(ColorSpace("RGB"),
                     np.round((np.array(rgb) + min_val) * 255).astype(np.uint8))

    @staticmethod
    def rgb2lab(self, color):
        color.value = color.value / 255.
        # Convert RGB to XYZ.
        red, green, blue = [val * 100. for val in
                            map(utility.rgb2xyz_nonlinear_transform,
                                color.value.tolist())]

        xyz = ColorSpaceConverter.RGB2XYZ_CONVERSION_MAT.dot(
            np.array([red, green, blue], dtype=np.float32))

        # Convert XYZ to Lab.
        xyz = np.divide(xyz, ColorSpaceConverter.WHITE_POINT)
        x_norm, y_norm, z_norm = map(utility.xyz2lab_nonlinear_transform,
                                     xyz.tolist())

        l = (116. * y_norm - 16.) * 255. / 100.
        a = 500. * (x_norm - y_norm) + 128
        b = 200. * (y_norm - z_norm) + 128

        return Color(ColorSpace("LAB"), np.round(np.array([l, a, b])).astype(np.uint8))

    @staticmethod
    def lab2rgb(self, color):
        l, a, b = color.value.tolist()
        # Convert Lab to XYZ.

        y = (l * 100. / 255. + 16.0) / 116.0
        x = (a - 128.) / 500. + y
        z = y - (b - 128.) / 200.

        xyz = np.multiply(
            map(utility.xyz2lab_nonlinear_transform_inv, [x, y, z]),
            ColorSpaceConverter.WHITE_POINT)

        # Convert XYZ to RGB.
        rgb = np.divide(
            inv(ColorSpaceConverter.RGB2XYZ_CONVERSION_MAT).dot(xyz), 100.)
        vec_func = np.vectorize(utility.rgb2xyz_nonlinear_transform_inv)
        rgb = np.multiply(vec_func(rgb), 255.)

        rgb[rgb < 0] = 0

        return Color(ColorSpace("RGB"), np.round(rgb).astype(np.uint8))

    def convert(self, color, dst_space):
        if color.space == dst_space:
            return color

        converter_name = "{}2{}".format(color.space, dst_space).lower()
        if hasattr(ColorSpaceConverter, converter_name):
            color_pair_func = getattr(ColorSpaceConverter, converter_name)
            return color_pair_func(self, color)
        else:
            raise InvalidConversion("no converter for: " + converter_name)
