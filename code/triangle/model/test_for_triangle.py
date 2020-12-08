import math
import unittest

from triangle.model.triangle import Triangle, TriangleError


class TriangleTests(unittest.TestCase):

    def test_check_constructor(self):
        test_triangle = Triangle(1, 1, 1, 0, 2, 1)
        self.assertTrue(test_triangle.x1 == 1 and test_triangle.x2 == 1 and test_triangle.x3 == 2)

    def test_get_ab(self):
        test_triangle = Triangle(0, 0, 0, 3, 4, 0)
        self.assertEqual(Triangle.get_ab(test_triangle), 3)

    def test_get_bc(self):
        test_triangle = Triangle(0, 0, 0, 3, 4, 0)
        self.assertEqual(Triangle.get_bc(test_triangle), 5)

    def test_get_ca(self):
        test_triangle = Triangle(0, 0, 0, 3, 4, 0)
        self.assertEqual(Triangle.get_ca(test_triangle), 4)

    def test_check_valid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 3, 4, 0)
        self.assertEqual(Triangle.is_triangle(test_triangle), True)

    def test_check_invalid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 1, 0, 2)
        self.assertEqual(Triangle.is_triangle(test_triangle), False)

    def test_get_area_valid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 3, 4, 0)
        self.assertEqual(Triangle.get_area(test_triangle), 6)

    def test_get_area_invalid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 1, 0, 2)
        with self.assertRaises(TriangleError):
            Triangle.get_area(test_triangle)

    def test_get_perimeter_valid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 3, 4, 0)
        self.assertEqual(Triangle.get_perimeter(test_triangle), 12)

    def test_get_perimeter_invalid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 1, 0, 2)
        with self.assertRaises(TriangleError):
            Triangle.get_perimeter(test_triangle)

    def test_get_circumcircle_radius_valid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 3, 4, 0)
        self.assertEqual(Triangle.get_circumcircle_radius(test_triangle), 2.5)

    def test_get_circumcircle_radius_invalid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 1, 0, 2)
        with self.assertRaises(TriangleError):
            Triangle.get_circumcircle_radius(test_triangle)

    def test_get_circumcircle_center_valid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 3, 4, 0)
        self.assertTrue((Triangle.get_circumcircle_center(test_triangle)[0] - 2.0) <= 1e-10 and
                        (Triangle.get_circumcircle_center(test_triangle)[1] - 1.5) <= 1e-10)

    def test_get_circumcircle_center_145221_valid_triangle(self):
        test_triangle = Triangle(1, 4, 5, 2, 2, 1)
        self.assertTrue((Triangle.get_circumcircle_center(test_triangle)[0] - 3.0) <= 1e-10 and
                        (Triangle.get_circumcircle_center(test_triangle)[1] - 3.0) <= 1e-10)

    def test_get_circumcircle_center_invalid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 1, 0, 2)
        with self.assertRaises(TriangleError):
            Triangle.get_circumcircle_center(test_triangle)

    def test_get_incircle_radius_valid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 3, 4, 0)
        self.assertEqual(Triangle.get_incircle_radius(test_triangle), 1.0)

    def test_get_incircle_radius_0006372_valid_triangle(self):
        test_triangle = Triangle(0, 0, 6, 0, 3, 7.2)
        self.assertEqual(Triangle.get_incircle_radius(test_triangle), 2.0)

    def test_get_incircle_radius_invalid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 1, 0, 2)
        with self.assertRaises(TriangleError):
            Triangle.get_incircle_radius(test_triangle)

    def test_get_incircle_center_valid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 3, 4, 0)
        self.assertTrue((Triangle.get_incircle_center(test_triangle)[0] - 1.0) <= 1e-10 and
                        (Triangle.get_incircle_center(test_triangle)[1] - 1.0) <= 1e-10)

    def test_get_incircle_center_0006372_valid_triangle(self):
        test_triangle = Triangle(0, 0, 6, 0, 3, 7.2)
        self.assertTrue((Triangle.get_incircle_center(test_triangle)[0] - 3.0) <= 1e-10 and
                        (Triangle.get_incircle_center(test_triangle)[1] - 2.0) <= 1e-10)

    def test_get_incircle_center_invalid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 1, 0, 2)
        with self.assertRaises(TriangleError):
            Triangle.get_incircle_center(test_triangle)

    def test_get_type_by_side_equilateral(self):
        test_triangle = Triangle(1, 1, 2, math.sqrt(3) + 1, 3, 1)
        self.assertEqual(Triangle.get_triangle_type_by_sides(test_triangle), "equilateral")

    def test_get_type_by_side_isosceles(self):
        test_triangle = Triangle(0, 0, 0, 1, 1, 0)
        self.assertEqual(Triangle.get_triangle_type_by_sides(test_triangle), "isosceles")

    def test_get_type_by_side_various(self):
        test_triangle = Triangle(0, 0, 0, 1, 2, 0)
        self.assertEqual(Triangle.get_triangle_type_by_sides(test_triangle), "various")

    def test_get_type_by_side_invalid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 1, 0, 2)
        with self.assertRaises(TriangleError):
            Triangle.get_triangle_type_by_sides(test_triangle)

    def test_get_type_by_angle_acute(self):
        test_triangle = Triangle(1, 1, 2, math.sqrt(3) + 1, 3, 1)
        self.assertEqual(Triangle.get_triangle_type_by_angles(test_triangle), "acute")

    def test_get_type_by_angle_right(self):
        test_triangle = Triangle(0, 0, 0, 3, 4, 0)
        self.assertEqual(Triangle.get_triangle_type_by_angles(test_triangle), "right")

    def test_get_type_by_angle_obtuse(self):
        test_triangle = Triangle(0, 0, 0, 3, 4, -1)
        self.assertEqual(Triangle.get_triangle_type_by_angles(test_triangle), "obtuse")


    def test_get_type_by_angle_invalid_triangle(self):
        test_triangle = Triangle(0, 0, 0, 1, 0, 2)
        with self.assertRaises(TriangleError):
            Triangle.get_triangle_type_by_angles(test_triangle)
