import unittest

from line_and_plane_intersection.viewmodel.viewmodel import ViewModel


class TestLinePlaneIntersectionViewModel(unittest.TestCase):
    def setUp(self):
        self.viewmodel = ViewModel()

    def test_1(self):
        self.assertEqual([0, 0, 0], self.viewmodel.get_x_y_z())

    def test_2(self):
        self.viewmodel.set_x_y_z([0, 1, 2])
        self.assertEqual([0, 0, 0], self.viewmodel.get_x_y_z())

    def test_3(self):
        self.viewmodel.set_current_point_for_line("line_point_1")
        self.viewmodel.set_x_y_z([0, 1, 2])
        self.assertEqual([0, 1, 2], self.viewmodel.get_x_y_z())

    def test_4(self):
        self.viewmodel.set_current_point_for_plane("line_point_1")
        self.viewmodel.set_x_y_z([0, 1, 2])
        self.assertEqual([0, 1, 2], self.viewmodel.get_x_y_z())

    def test_5(self):
        self.viewmodel.set_current_point_for_line("line_point_1")
        self.viewmodel.set_x_y_z([1, 5, -1])
        self.viewmodel.set_current_point_for_line("line_point_2")
        self.viewmodel.set_x_y_z([4, 3, 3])

        self.viewmodel.set_current_point_for_plane("plane_point_1")
        self.viewmodel.set_x_y_z([1, 12, 1])
        self.viewmodel.set_current_point_for_plane("plane_point_2")
        self.viewmodel.set_x_y_z([1, 1, 1])
        self.viewmodel.set_current_point_for_plane("plane_point_3")
        self.viewmodel.set_x_y_z([1, 13, 1])

        self.viewmodel.is_intercept()

        self.assertEqual('True', self.viewmodel.interception_or_error_msg)

    def test_6(self):
        self.viewmodel.set_current_point_for_line("line_point_1")
        self.viewmodel.set_x_y_z([1, 5, -1])

        self.viewmodel.set_current_point_for_plane("plane_point_1")
        self.viewmodel.set_x_y_z([1, 12, 1])
        self.viewmodel.set_current_point_for_plane("plane_point_2")
        self.viewmodel.set_x_y_z([1, 1, 1])
        self.viewmodel.set_current_point_for_plane("plane_point_3")
        self.viewmodel.set_x_y_z([1, 13, 1])

        self.viewmodel.is_intercept()

        self.assertEqual('Not completed points.', self.viewmodel.interception_or_error_msg)

    def test_7(self):
        self.viewmodel.set_current_point_for_line("line_point_1")
        self.viewmodel.set_x_y_z([1, 5, -1])
        self.viewmodel.set_current_point_for_line("line_point_2")
        self.viewmodel.set_x_y_z([1, 5, -1])

        self.viewmodel.set_current_point_for_plane("plane_point_1")
        self.viewmodel.set_x_y_z([1, 12, 1])
        self.viewmodel.set_current_point_for_plane("plane_point_2")
        self.viewmodel.set_x_y_z([1, 1, 1])
        self.viewmodel.set_current_point_for_plane("plane_point_3")
        self.viewmodel.set_x_y_z([1, 13, 1])

        self.viewmodel.is_intercept()

        self.assertIn('Line is defined by two different points', self.viewmodel.interception_or_error_msg)
