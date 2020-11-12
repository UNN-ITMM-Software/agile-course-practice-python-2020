import unittest

from lines_intersect.model.lines_intersect import determine_if_two_line_segments_intersect


class TestFractionClass(unittest.TestCase):
    def test_can_det_if_two_lines_intersect(self):
        line1 = ((0, 0), (1, 1))
        line2 = ((0, 1), (1, 0))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_two_lines_do_not_intersect(self):
        line1 = ((0, 0), (0, 1))
        line2 = ((1, 0), (1, 1))
        self.assertFalse(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_two_parallel_lines_do_not_intersect(self):
        line1 = ((0, 0), (1, 0))
        line2 = ((0, 1), (1, 1))
        self.assertFalse(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_overlapping_lines_intersect(self):
        line1 = ((0, 0), (1, 0))
        line2 = ((0.5, 0), (1.5, 0))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_equal_lines_intersect(self):
        line1 = ((0, 0), (1, 0))
        line2 = ((0, 0), (1, 0))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_not_overlapping_parallel_x_lines_do_not_intersect(self):
        line1 = ((0, 0), (1, 0))
        line2 = ((2, 0), (3, 0))
        self.assertFalse(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_not_overlapping_parallel_y_lines_do_not_intersect(self):
        line1 = ((0, 0), (0, 1))
        line2 = ((0, 2), (0, 3))
        self.assertFalse(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_not_overlapping_parallel_lines_do_not_intersect(self):
        line1 = ((0, 0), (1, 1))
        line2 = ((-2, -2), (-3, -3))
        self.assertFalse(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_parallel_lines_with_common_edge_intersect(self):
        line1 = ((0, 0), (1, 1))
        line2 = ((1, 1), (3, 3))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_unequal_points_do_not_intersect(self):
        point1 = ((0, 0), (0, 0))
        point2 = ((0.1, 0.1), (0.1, 0.1))
        self.assertFalse(determine_if_two_line_segments_intersect(point1, point2))

    def test_can_det_if_equal_points_intersect(self):
        point = ((0.1, -0.1), (0.1, -0.1))
        self.assertTrue(determine_if_two_line_segments_intersect(point, point))

    def test_can_det_if_line_segments_with_common_edge_point_intersect(self):
        line1 = ((0, 0), (0.1, 0.1))
        line2 = ((0.05, 0.05), (0, 0.1))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_line_segments_with_common_edges_intersect(self):
        line1 = ((0, 0), (0.1, 0.1))
        line2 = ((0.05, 0), (0.1, 0.1))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_point_and_line_segment_intersect_1(self):
        line1 = ((0, 0), (0, 0))
        line2 = ((-0.05, -0.05), (0.1, 0.1))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_if_point_and_line_segment_intersect_2(self):
        line1 = ((-0.05, -0.05), (0.1, 0.1))
        line2 = ((0, 0), (0, 0))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))

    def test_can_det_intersection_if_float_numbers_are_large(self):
        line1 = ((0, 0), (0, 1e10))
        line2 = ((0, 1e10), (0, 2e10))
        self.assertTrue(determine_if_two_line_segments_intersect(line1, line2))
