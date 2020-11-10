import unittest

from line_and_plane_intersection.model.intersection import Point3D
from line_and_plane_intersection.model.intersection import Plane


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
