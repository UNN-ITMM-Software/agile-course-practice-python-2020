import unittest

from levitsky_ilya_lab1 import calculating_volume_3d_figures as vol


class TestCalculatingVolume(unittest.TestCase):

    def test_calculate_volume_cube_default(self):
        result = vol.calculate_volume_cube()
        self.assertEqual(result, 1)

    def test_calculate_volume_cube_0(self):
        result = vol.calculate_volume_cube(0)
        self.assertEqual(result, 0)

    def test_calculate_volume_cube_3(self):
        result = vol.calculate_volume_cube(3)
        self.assertEqual(result, 27)

    def test_calculate_volume_cube_negative(self):
        with self.assertRaises(ValueError):
            vol.calculate_volume_cube(-9)

    def test_calculate_volume_sphere_default(self):
        result = vol.calculate_volume_sphere()
        self.assertEqual(result, 4.189)

    def test_calculate_volume_sphere_0(self):
        result = vol.calculate_volume_sphere(0)
        self.assertEqual(result, 0)

    def test_calculate_volume_sphere_10(self):
        result = vol.calculate_volume_sphere(10)
        self.assertEqual(result, 4188.79)

    def test_calculate_volume_sphere_negative(self):
        with self.assertRaises(ValueError):
            vol.calculate_volume_sphere(-5)

    def test_calculate_volume_cylinder_default(self):
        result = vol.calculate_volume_cylinder()
        self.assertEqual(result, 3.142)

    def test_calculate_volume_cylinder_0(self):
        result = vol.calculate_volume_cylinder(0)
        self.assertEqual(result, 0)

    def test_calculate_volume_cylinder_2_3(self):
        result = vol.calculate_volume_cylinder(2, 3)
        self.assertEqual(result, 37.699)

    def test_calculate_volume_cylinder_negative_radius(self):
        with self.assertRaises(ValueError):
            vol.calculate_volume_cylinder(2, -3)

    def test_calculate_volume_cylinder_negative_height(self):
        with self.assertRaises(ValueError):
            vol.calculate_volume_cylinder(-2, 3)
