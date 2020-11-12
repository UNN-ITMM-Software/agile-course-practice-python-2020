import numpy as np


class Line:
    def __init__(self, point1, point2):
        """Create a line segment.

        Keyword arguments:
        point1 -- the first point of line segment
        point2 -- the second point of line segment

        A point is a tuple of two real numbers (x, y).

        """
        try:
            x1, y1 = point1
            x2, y2 = point2
            for value in [x1, y1, x2, y2]:
                if not type(value) in [int, float]:
                    raise TypeError
        except:
            raise TypeError("Point must be a tuple of two real numbers")
        self.point1 = (float(point1[0]), float(point1[1]))
        self.point2 = (float(point2[0]), float(point2[1]))


def determine_if_two_line_segments_intersect(line_segment_1, line_segment_2):
    """Determine if two line segments intersect.

    Keyword arguments:
    line_segment_1 -- the first line segment
    line_segment_2 -- the second line segment

    Returns:
    True of False

    A point is a pair of two real numbers (x, y).
    Two line segments do not intersect if they have no common points.

    """
    p11, p12 = (line_segment_1.point1, line_segment_1.point2)
    p21, p22 = (line_segment_2.point1, line_segment_2.point2)

    inv_matrix = np.array([[p21[1]-p22[1], p22[0]-p21[0]],
                           [p11[1]-p12[1], p12[0]-p11[0]]], dtype=np.float64)
    det = np.linalg.det(inv_matrix)

    def is_float_eq(a, b):
        return np.isclose(a, b, rtol=1e-10, atol=1e-12)

    def is_float_between(a, c1, c2):
        return is_float_eq(a, c1) or is_float_eq(a, c2) or c1 < a < c2

    if is_float_eq(det, 0.0):  # line segments are parallel
        if not is_float_eq(np.linalg.det(np.array([[p11[0]-p21[0], p11[0]-p12[0]],
                                                   [p11[1]-p21[1], p11[1]-p12[1]]],
                                                  dtype=np.float64)), 0.0):
            return False

        def is_point_on_line(point, line):
            check_x = is_float_between(point[0], line.point1[0], line.point2[0])
            check_y = is_float_between(point[1], line.point1[1], line.point2[1])
            return check_x and check_y

        check_line1 = is_point_on_line(p11, line_segment_2) or is_point_on_line(p12, line_segment_2)
        check_line2 = is_point_on_line(p21, line_segment_1) or is_point_on_line(p22, line_segment_1)
        return check_line1 or check_line2

    vector = np.array([p21[0]-p11[0], p21[1]-p11[1]], dtype=np.float64)
    params = np.dot(inv_matrix, vector) / det
    return is_float_between(params[0], 0, 1) and is_float_between(params[1], 0, 1)
