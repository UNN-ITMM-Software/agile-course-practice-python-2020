import numpy as np


def determine_if_two_line_segments_intersect(line_segment_1, line_segment_2):
    """Determine if two line segments intersect.

    Keyword arguments:
    line_segment_1 -- the first line segment (a pair of two points)
    line_segment_2 -- the second line segment (a pair of two points)

    Returns:
    True of False

    A point is a pair of two real numbers (x, y).
    Two line segments do not intersect if they have no common points.

    """
    p11, p12 = line_segment_1
    p21, p22 = line_segment_2

    inv_matrix = np.array([[p21[1]-p22[1], p22[0]-p21[0]],
                           [p11[1]-p12[1], p12[0]-p11[0]]])
    det = np.linalg.det(inv_matrix)

    if det == 0:  # line segments are parallel
        if np.linalg.det([[p11[0]-p21[0], p11[0]-p12[0]],
                          [p11[1]-p21[1], p11[1]-p12[1]]]) != 0:
            return False

        def is_point_on_line(point, line):
            return line[0][0] <= point[0] <= line[1][0] and line[0][1] <= point[1] <= line[1][1]

        check_line1 = is_point_on_line(p11, line_segment_2) or is_point_on_line(p12, line_segment_2)
        check_line2 = is_point_on_line(p21, line_segment_1) or is_point_on_line(p22, line_segment_1)
        return check_line1 or check_line2

    vector = np.array([p21[0]-p11[0], p21[1]-p11[1]])
    params = np.dot(inv_matrix, vector) / det
    return 0 <= params[0] <= 1 and 0 <= params[1] <= 1
