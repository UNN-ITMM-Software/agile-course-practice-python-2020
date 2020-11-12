import unittest

from lines_intersect.model.lines_intersect import determine_if_two_line_segments_intersect, Line


class TestLineClass(unittest.TestCase):
    def test_can_not_create_line_if_point_is_not_a_pair(self):
        point1 = (1, 2)
        point2 = (1, 2, 3)
        self.assertRaises(TypeError, Line, point1, point2)

    def test_can_not_create_line_if_coordinate_has_not_a_correct_type(self):
        point1 = ("1", 2)
        point2 = (1, 2.0)
        self.assertRaises(TypeError, Line, point1, point2)

    def test_can_create_line_if_args_are_correct(self):
        point1 = (3.0, 2.0)
        point2 = (1.0, 2.0)
        line = Line(point1, point2)
        self.assertTrue(point1 == line.point1 and point2 == line.point2)

    def test_points_of_created_line_are_float_numbers(self):
        point1 = (3.0, 2.0)
        point2 = (1, 2.0)
        line = Line(point1, point2)
        self.assertIsInstance(line.point2[0], float)


class TestTwoLinesIntersection(unittest.TestCase):
    def test_can_det_if_two_lines_intersect(self):
        line1 = Line((0, 0), (1, 1))
        line2 = Line((0, 1), (1, 0))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_two_lines_do_not_intersect(self):
        line1 = Line((0, 0), (0, 1))
        line2 = Line((1, 0), (1, 1))
        self.assertFalse(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_two_parallel_lines_do_not_intersect(self):
        line1 = Line((0, 0), (1, 0))
        line2 = Line((0, 1), (1, 1))
        self.assertFalse(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_overlapping_lines_intersect(self):
        line1 = Line((0, 0), (1, 0))
        line2 = Line((0.5, 0), (1.5, 0))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_equal_lines_intersect(self):
        line1 = Line((0, 0), (1, 0))
        line2 = Line((0, 0), (1, 0))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_not_overlapping_parallel_x_lines_do_not_intersect(self):
        line1 = Line((0, 0), (1, 0))
        line2 = Line((2, 0), (3, 0))
        self.assertFalse(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_not_overlapping_parallel_y_lines_do_not_intersect(self):
        line1 = Line((0, 0), (0, 1))
        line2 = Line((0, 2), (0, 3))
        self.assertFalse(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_not_overlapping_parallel_lines_do_not_intersect(self):
        line1 = Line((0, 0), (1, 1))
        line2 = Line((-2, -2), (-3, -3))
        self.assertFalse(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_parallel_lines_with_common_edge_intersect(self):
        line1 = Line((0, 0), (1, 1))
        line2 = Line((1, 1), (3, 3))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_unequal_points_do_not_intersect(self):
        point1 = Line((0, 0), (0, 0))
        point2 = Line((0.1, 0.1), (0.1, 0.1))
        self.assertFalse(determine_if_two_line_segments_intersect(point1, point2))

    def test_can_det_if_equal_points_intersect(self):
        point = Line((0.1, -0.1), (0.1, -0.1))
        self.assertTrue(determine_if_two_line_segments_intersect(point, point))

    def test_can_det_if_line_segments_with_common_edge_point_intersect(self):
        line1 = Line((0, 0), (0.1, 0.1))
        line2 = Line((0.05, 0.05), (0, 0.1))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_line_segments_with_common_edges_intersect(self):
        line1 = Line((0, 0), (0.1, 0.1))
        line2 = Line((0.05, 0), (0.1, 0.1))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_point_and_line_segment_intersect_1(self):
        line1 = Line((0, 0), (0, 0))
        line2 = Line((-0.05, -0.05), (0.1, 0.1))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_point_and_line_segment_intersect_2(self):
        line1 = Line((-0.05, -0.05), (0.1, 0.1))
        line2 = Line((0, 0), (0, 0))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_intersection_if_float_numbers_are_large(self):
        line1 = Line((0, 0), (0, 1e10))
        line2 = Line((0, 1e10), (0, 2e10))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))
