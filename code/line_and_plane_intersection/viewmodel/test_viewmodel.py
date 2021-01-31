import unittest

from line_and_plane_intersection.viewmodel.viewmodel import ViewModel
from line_and_plane_intersection.logger.fakelogger import FakeLogger
from line_and_plane_intersection.logger.reallogger import RealLogger


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


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = ViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Line-Plane intersection application init',
                         self.view_model.logger.get_last_message())

    def test_logging_set_current_plane_point(self):
        self.view_model.set_current_point_for_plane("plane_point_1")
        self.assertEqual('Current plane point = plane_point_1',
                         self.view_model.logger.get_last_message())

    def test_logging_set_current_line_point(self):
        self.view_model.set_current_point_for_line("line_point_1")
        self.assertEqual('Current line point = line_point_1',
                         self.view_model.logger.get_last_message())

    def test_logging_set_line_xyz(self):
        self.view_model.set_current_point_for_line("line_point_1")
        self.view_model.set_x_y_z([1, 2, 3])
        self.assertEqual('dict_type = line, x_y_z set = [1, 2, 3]',
                         self.view_model.logger.get_last_message())

    def test_logging_set_plane_xyz(self):
        self.view_model.set_current_point_for_plane("plane_point_1")
        self.view_model.set_x_y_z([1, 2, 3])
        self.assertEqual('dict_type = plane, x_y_z set = [1, 2, 3]',
                         self.view_model.logger.get_last_message())

    def test_logging_set_abcd(self):
        self.view_model.set_abcd([2, -3, -3, 12])
        self.assertEqual('abcd set = [2, -3, -3, 12]', self.view_model.logger.get_last_message())

    def test_logging_intersection_check(self):
        expected_messages = ['Line-Plane intersection application init',
                             'Current line point = line_point_1',
                             'dict_type = line, x_y_z set = [0, 5, -1]',
                             'Current line point = line_point_2',
                             'dict_type = line, x_y_z set = [3, 3, 3]',
                             'Current plane point = plane_point_1',
                             'dict_type = plane, x_y_z set = [1, 12, 1]',
                             'Current plane point = plane_point_2',
                             'dict_type = plane, x_y_z set = [1, 1, 1]',
                             'Current plane point = plane_point_3',
                             'dict_type = plane, x_y_z set = [1, 13, 1]',
                             'abcd set = [2, -3, -3, 12]',
                             'Get result: True']

        self.view_model.set_current_point_for_line("line_point_1")
        self.view_model.set_x_y_z([0, 5, -1])
        self.view_model.set_current_point_for_line("line_point_2")
        self.view_model.set_x_y_z([3, 3, 3])
        self.view_model.set_current_point_for_plane("plane_point_1")
        self.view_model.set_x_y_z([1, 12, 1])
        self.view_model.set_current_point_for_plane("plane_point_2")
        self.view_model.set_x_y_z([1, 1, 1])
        self.view_model.set_current_point_for_plane("plane_point_3")
        self.view_model.set_x_y_z([1, 13, 1])
        self.view_model.set_abcd([2, -3, -3, 12])
        self.view_model.is_intersect()
        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages())

    def test_logging_intersection_check_incorrect_case(self):
        expected_messages = ['Line-Plane intersection application init',
                             'Current line point = line_point_1',
                             'dict_type = line, x_y_z set = [1, 5, -1]',
                             'Current line point = line_point_2',
                             'dict_type = line, x_y_z set = [1, 5, -1]',
                             'Current plane point = plane_point_1',
                             'dict_type = plane, x_y_z set = [1, 12, 1]',
                             'Current plane point = plane_point_2',
                             'dict_type = plane, x_y_z set = [1, 1, 1]',
                             'Current plane point = plane_point_3',
                             'dict_type = plane, x_y_z set = [1, 13, 1]',
                             'abcd set = [2, -3, -3, 12]',
                             'Get result: Line::init - Incorrect value. '
                             'Line is defined by two different points']

        self.view_model.set_current_point_for_line("line_point_1")
        self.view_model.set_x_y_z([1, 5, -1])
        self.view_model.set_current_point_for_line("line_point_2")
        self.view_model.set_x_y_z([1, 5, -1])
        self.view_model.set_current_point_for_plane("plane_point_1")
        self.view_model.set_x_y_z([1, 12, 1])
        self.view_model.set_current_point_for_plane("plane_point_2")
        self.view_model.set_x_y_z([1, 1, 1])
        self.view_model.set_current_point_for_plane("plane_point_3")
        self.view_model.set_x_y_z([1, 13, 1])
        self.view_model.set_abcd([2, -3, -3, 12])
        self.view_model.is_intersect()
        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages())

    def test_logging_intersection_check_not_completed_points_case(self):
        expected_messages = ['Line-Plane intersection application init',
                             'Current line point = line_point_1',
                             'dict_type = line, x_y_z set = [1, 5, -1]',
                             'Current plane point = plane_point_1',
                             'dict_type = plane, x_y_z set = [1, 12, 1]',
                             'Current plane point = plane_point_2',
                             'dict_type = plane, x_y_z set = [1, 1, 1]',
                             'Current plane point = plane_point_3',
                             'dict_type = plane, x_y_z set = [1, 13, 1]',
                             'Get result: Not completed points.']

        self.view_model.set_current_point_for_line("line_point_1")
        self.view_model.set_x_y_z([1, 5, -1])
        self.view_model.set_current_point_for_plane("plane_point_1")
        self.view_model.set_x_y_z([1, 12, 1])
        self.view_model.set_current_point_for_plane("plane_point_2")
        self.view_model.set_x_y_z([1, 1, 1])
        self.view_model.set_current_point_for_plane("plane_point_3")
        self.view_model.set_x_y_z([1, 13, 1])
        self.view_model.is_intersect()
        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages())


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = ViewModel(RealLogger())
