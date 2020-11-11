import unittest

from line_and_plane_intersection.model.intersection import Point3D
from line_and_plane_intersection.model.intersection import Plane
from line_and_plane_intersection.model.intersection import Line
from line_and_plane_intersection.model.intersection import Intersection


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

    def test_cannot_create_plane_with_points_on_same_line(self):
        p1 = Point3D(-2, 0, 3)
        p2 = Point3D(2, 1, -2)
        p3 = Point3D(38, 10, -47)
        self.assertRaises(ValueError, Plane, p1, p2, p3)

    def test_correct_canonical_view(self):
        p1 = Point3D(1, -2, 0)
        p2 = Point3D(2, 0, -1)
        p3 = Point3D(0, -1, 2)

        plane = Plane(p1, p2, p3)

        self.assertEqual(plane.abcd, (5, -1, 3, -7))

    def test_point_on_plane_one(self):
        p1 = Point3D(1, -2, 0)
        p2 = Point3D(2, 0, -1)
        p3 = Point3D(0, -1, 2)
        plane = Plane(p1, p2, p3)
        self.assertTrue(plane.point_on_plane(Point3D(1, -2, 0)))

    def test_point_on_plane_two(self):
        p1 = Point3D(1, -2, 0)
        p2 = Point3D(2, 0, -1)
        p3 = Point3D(0, -1, 2)
        plane = Plane(p1, p2, p3)
        self.assertFalse(plane.point_on_plane(Point3D(1, -2, 99999)))

    def test_can_get_describe(self):
        p1 = Point3D(1, -2, 0)
        p2 = Point3D(2, 0, -1)
        p3 = Point3D(0, -1, 2)
        plane = Plane(p1, p2, p3)

        describe = plane.get_describe()

        self.assertEqual(describe, (5, -1, 3, -7))


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

    def test_can_get_describe(self):
        p1 = Point3D(-2, 0, 3)
        p2 = Point3D(2, 1, -2)
        line = Line(p1, p2)

        describe = line.get_describe()

        self.assertEqual(describe, (Point3D(-2, 0, 3), Point3D(4, 1, -5)))


class TestIntersection(unittest.TestCase):
    def test_intersection_one(self):
        line = Line(Point3D(0, 5, -1), Point3D(3, 3, 3))
        plane = Plane(Point3D(1, 12, 1), Point3D(1, 1, 1), Point3D(1, 13, 1))
        plane.abcd = (2, -3, -3, 12)    # dirty hack i know
        self.assertTrue(Intersection.have_intersection(line, plane))

    def test_intersection_two(self):
        line = Line(Point3D(-2, 3, -1), Point3D(-1, 6, 1))
        plane = Plane(Point3D(1, 12, 1), Point3D(1, 1, 1), Point3D(1, 13, 1))
        plane.abcd = (0, 2, -1, -11)    # dirty hack i know
        self.assertTrue(Intersection.have_intersection(line, plane))

    def test_intersection_three(self):
        line = Line(Point3D(1, 5, -1), Point3D(4, 3, 3))
        plane = Plane(Point3D(1, 12, 1), Point3D(1, 1, 1), Point3D(1, 13, 1))
        plane.abcd = (2, -3, -3, 12)    # dirty hack i know
        self.assertFalse(Intersection.have_intersection(line, plane))
