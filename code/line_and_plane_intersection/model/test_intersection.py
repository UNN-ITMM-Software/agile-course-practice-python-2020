import unittest

from line_and_plane_intersection.model.intersection import Point3D
from line_and_plane_intersection.model.intersection import Plane
from line_and_plane_intersection.model.intersection import Line


class TestPoint3D(unittest.TestCase):
    def test_can_create_point_from_xyz(self):
        self.assertEqual(Point3D(3, 4, 5).to_tuple(), (3, 4, 5))

    def test_can_create_point_from_list(self):
        self.assertEqual(Point3D([3, 4, 5]).to_tuple(), (3, 4, 5))

    def test_can_create_point_from_tuple(self):
        self.assertEqual(Point3D((3, 4, 5)).to_tuple(), (3, 4, 5))

    def test_can_create_point_from_other_point(self):
        p = Point3D((3, 4, 5))
        self.assertEqual(Point3D(p).to_tuple(), (3, 4, 5))

    def test_cannot_create_point_on_plane(self):
        self.assertRaises(ValueError, Point3D, (2, 2))

    def test_cannot_create_from_list_of_tuple(self):
        self.assertRaises(TypeError, Point3D, [(2,), (2,), (3,)])

    def test_cannot_create_from_tuple_of_list(self):
        self.assertRaises(TypeError, Point3D, ([2], [2], [3]))

    def test_cannot_create_from_str(self):
        self.assertRaises(TypeError, Point3D, 'str')

    def test_can_get_point_str(self):
        self.assertEqual(str(Point3D(3, 4, 5)), 'Point3D [x: 3, y: 4, z: 5]')

    def test_can_compare_two_points(self):
        p1 = Point3D(1, 0, 1)
        p2 = Point3D(p1)
        self.assertTrue(p1 == p2)

    def test_can_sub_point_one(self):
        p1 = Point3D(1, -47, 23)
        p2 = Point3D(-43, 27, 12)
        self.assertEqual(p1 - p2, Point3D(44, -74, 11))

    def test_can_sub_point_two(self):
        p1 = Point3D(1, -47, 23)
        p2 = Point3D(-43, 27, 12)
        self.assertEqual(p2 - p1, Point3D(-44, 74, -11))


class TestPlane(unittest.TestCase):
    def test_can_create_plane(self):
        p1 = Point3D(0, 0, 0)
        p2 = Point3D(1, 1, 1)
        p3 = Point3D(1, 0, 1)

        plane = Plane(p1, p2, p3)

        self.assertEqual([plane.p1, plane.p2, plane.p3], [p1, p2, p3])

    def test_can_change_source_data(self):
        p1 = Point3D(0, 0, 0)
        p2 = Point3D(1, 1, 1)
        p3 = Point3D(1, 0, 1)
        plane = Plane(p1, p2, p3)

        p1.x = 99999

        self.assertNotEqual([plane.p1, plane.p2, plane.p3], [p1, p2, p3])

    def test_cannot_create_plane_from_int(self):
        self.assertRaises(TypeError, Plane, 5, 5, 5)

    def test_cannot_create_plane_with_similar_points(self):
        p1 = Point3D(0, 0, 0)
        p2 = Point3D(p1)
        p3 = Point3D(1, 0, 1)
        self.assertRaises(ValueError, Plane, p1, p2, p3)


class TestLine(unittest.TestCase):
    def test_can_create_line(self):
        p1 = Point3D(0, 0, 0)
        p2 = Point3D(1, 1, 1)

        line = Line(p1, p2)

        self.assertEqual([line.p1, line.p2], [p1, p2])

    def test_can_change_source_data(self):
        p1 = Point3D(0, 0, 0)
        p2 = Point3D(1, 1, 1)
        line = Line(p1, p2)

        p1.x = 99999

        self.assertNotEqual([line.p1, line.p2], [p1, p2])

    def test_cannot_create_line_from_int(self):
        self.assertRaises(TypeError, Line, 5, 5)

    def test_cannot_create_line_with_similar_points(self):
        p1 = Point3D(0, 0, 0)
        p2 = Point3D(p1)
        self.assertRaises(ValueError, Line, p1, p2)

    def test_point_on_line_one(self):
        line = Line(Point3D(2, -3, 6), Point3D(4, -3, -10))
        point = Point3D(2, -3, 6)
        self.assertTrue(line.point_on_line(point))

    def test_point_on_line_two(self):
        line = Line(Point3D(2, -3, 6), Point3D(4, -3, -10))
        point = Point3D(2, -2, 6)
        self.assertFalse(line.point_on_line(point))

    def test_point_on_line_three(self):
        line = Line(Point3D(2, -3, 6), Point3D(4, -3, 6))
        point = Point3D(2, -3, 6)
        self.assertTrue(line.point_on_line(point))

    def test_point_on_line_four(self):
        line = Line(Point3D(4, -3, 6), Point3D(4, -3, -10))
        point = Point3D(4, -3, 6)
        self.assertTrue(line.point_on_line(point))

    def test_point_on_line_five(self):
        line = Line(Point3D(4, -3, 6), Point3D(4, -3, -10))
        point = Point3D(5, -3, 6)
        self.assertFalse(line.point_on_line(point))

    def test_point_on_line_six(self):
        line = Line(Point3D(2, -3, 6), Point3D(4, -3, 6))
        point = Point3D(2, -3, 7)
        self.assertFalse(line.point_on_line(point))

    def test_point_on_line_seven(self):
        line = Line(Point3D(-2, 0, 3), Point3D(2, 1, -2))
        point = Point3D(2, 1, -2)
        self.assertTrue(line.point_on_line(point))
