import unittest

from line_and_plane_intersection.viewmodel.viewmodel import ViewModel


class TestLinePlaneIntersectionViewModel(unittest.TestCase):
    def setUp(self):
        self.viewmodel = ViewModel()

    def test_get_with_not_correct_state(self):
        self.assertEqual([0, 0, 0], self.viewmodel.get_x_y_z())

    def test_set_and_get_with_not_correct_state(self):
        self.viewmodel.set_x_y_z([0, 1, 2])
        self.assertEqual([0, 0, 0], self.viewmodel.get_x_y_z())

    def test_set_line_point(self):
        self.viewmodel.set_current_point_for_line("line_point_1")
        self.viewmodel.set_x_y_z([0, 1, 2])
        self.assertEqual([0, 1, 2], self.viewmodel.get_x_y_z())

    def test_set_plane_point(self):
        self.viewmodel.set_current_point_for_plane("plane_point_1")
        self.viewmodel.set_x_y_z([0, 1, 2])
        self.assertEqual([0, 1, 2], self.viewmodel.get_x_y_z())

    def test_correct_intersect_false(self):
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
        self.viewmodel.set_abcd([2, -3, -3, 12])

        self.viewmodel.is_intersect()

        self.assertEqual('False', self.viewmodel.interception_or_error_msg)

    def test_not_correct_intersect_missed_point(self):
        self.viewmodel.set_current_point_for_line("line_point_1")
        self.viewmodel.set_x_y_z([1, 5, -1])

        self.viewmodel.set_current_point_for_plane("plane_point_1")
        self.viewmodel.set_x_y_z([1, 12, 1])
        self.viewmodel.set_current_point_for_plane("plane_point_2")
        self.viewmodel.set_x_y_z([1, 1, 1])
        self.viewmodel.set_current_point_for_plane("plane_point_3")
        self.viewmodel.set_x_y_z([1, 13, 1])

        self.viewmodel.is_intersect()

        self.assertEqual('Not completed points.', self.viewmodel.interception_or_error_msg)

    def test_not_correct_intersect_incorrect_line(self):
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
        self.viewmodel.set_abcd([2, -3, -3, 12])

        self.viewmodel.is_intersect()

        self.assertIn('Line is defined by two different points', self.viewmodel.interception_or_error_msg)

    def test_correct_intersect_true(self):
        self.viewmodel.set_current_point_for_line("line_point_1")
        self.viewmodel.set_x_y_z([0, 5, -1])
        self.viewmodel.set_current_point_for_line("line_point_2")
        self.viewmodel.set_x_y_z([3, 3, 3])

        self.viewmodel.set_current_point_for_plane("plane_point_1")
        self.viewmodel.set_x_y_z([1, 12, 1])
        self.viewmodel.set_current_point_for_plane("plane_point_2")
        self.viewmodel.set_x_y_z([1, 1, 1])
        self.viewmodel.set_current_point_for_plane("plane_point_3")
        self.viewmodel.set_x_y_z([1, 13, 1])
        self.viewmodel.set_abcd([2, -3, -3, 12])

        self.viewmodel.is_intersect()

        self.assertEqual('True', self.viewmodel.interception_or_error_msg)
