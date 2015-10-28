import unittest

from matrix import Matrix


class MatrixTests(unittest.TestCase):

    def test_check_constructor(self):
        test_matrix = Matrix.make_from_list([[1, 1]])
        if test_matrix.cols == 2 and test_matrix.rows == 1:
            if test_matrix.data_lines[0][0] ==\
                    test_matrix.data_lines[0][1] == 1:
                    self.assertEqual(1, 1)

    def test_can_calculate_determinant_for_matrix1x1(self):
        test_matrix = Matrix.make_random(1, 1)
        det = Matrix.calculate_det(test_matrix)
        self.assertTrue(test_matrix.data_lines[0][0] == det)

    def test_check_str_func(self):
        test_matrix = Matrix.make_from_list([[1, 3], [5, 7]])
        s = test_matrix.__str__()
        self.assertEqual(s, '1 3\n5 7\n')

    def test_is_matrix_square(self):
        test_matrix = Matrix.make_random(3, 3)
        self.assertEqual(test_matrix.is_matrix_square(), 1)

    def test_is_matrix_not_square(self):
        test_matrix = Matrix.make_random(3, 2)
        self.assertEqual(test_matrix.is_matrix_square(), 0)

    def test_can_calculate_determinant_for_matrix2x2(self):
        test_matrix = Matrix.make_from_list([[1, 3], [5, 7]])
        det = Matrix.calculate_det(test_matrix)
        self.assertEqual(det, -8)

    def test_delete_zero_row_and_zero_col_in_matrix(self):
        test_matrix = Matrix.make_from_list([[1, 3], [5, 7]])
        det = Matrix.calculate_det(Matrix.del_col_and_row(
            test_matrix, 0, 0))
        self.assertEqual(det, 7)

    def test_can_calculate_determinant_for_matrix3x3(self):
        test_matrix = Matrix.make_from_list([[7, 2, 0], [5, 8, 7], [1, 2, 3]])
        det = Matrix.calculate_det(test_matrix)
        self.assertEqual(det, 54)

    def test_can_calculate_determinant_with_second_col_decompos(self):
        test_matrix = Matrix.make_from_list([[1, 0, -3], [0, 0, 2],
                                             [-1, -2, 0]])
        det = Matrix.calculate_det(Matrix.del_col_and_row(test_matrix, 0, 1))
        self.assertEqual(det, 2)

    def test_can_calculate_determinant_for_matrix6x6(self):
        test_matrix = Matrix.make_from_list([[-1, 2, 3, 4, 5, 6],
                                             [7, 0, 4, -1, 0, -3],
                                             [0, 5, -6, 0, 0, 3],
                                             [1, 0, 3, 4, 5, 6],
                                             [0, 8, 0, 1, 2, 0],
                                             [-4, 0, 6, 0, 0, -5]])
        det = Matrix.calculate_det(test_matrix)
        self.assertEqual(det, -96)


