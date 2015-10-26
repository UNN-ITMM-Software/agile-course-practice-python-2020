import unittest
from main.matrix import Matrix


class MatrixTests(unittest.TestCase):

    def test_can_calculate_determinant_for_matrix1x1(self):
        test_matrix = Matrix.make_random(1, 1)
        det = Matrix.calculate_det(test_matrix)
        self.assertTrue(test_matrix.data_lines[0][0] == det)

    def test_is_matrix_square(self):
        test_matrix = Matrix.make_random(3, 3)
        self.assertTrue(test_matrix.rows == test_matrix.cols)

    def test_can_calculate_determinant_for_matrix2x2(self):
        test_matrix = Matrix.make_from_list([[1, 3], [5, 7]])
        det = Matrix.calculate_det(test_matrix)
        self.assertEqual(det, -8)

    def test_delete_zero_row_and_zero_col_in_matrix(self):
        test_matrix = Matrix.make_from_list([[1, 3], [5, 7]])
        det = Matrix.calculate_det(Matrix.delete_col_and_row(
            test_matrix, 0, 0))
        self.assertEqual(det, 7)

    def test_can_calculate_determinant_for_matrix3x3(self):
        test_matrix = Matrix.make_from_list([[7, 2, 0], [5, 8, 7], [1, 2, 3]])
        det = Matrix.calculate_det(test_matrix)
        self.assertEqual(det, 54)

    def test_can_calculate_determinant_with_second_column_decomposition(self):
        test_matrix = Matrix.make_from_list([[1, 0, -3], [0, 0, 2], [-1, -2, 0]])
        det = Matrix.calculate_det(Matrix.delete_col_and_row(test_matrix, 0, 1))
        self.assertEqual(det, 2)

    def test_can_calculate_determinant_for_matrix6x6(self):
        test_matrix = Matrix.make_from_list([[-1, 2, 3, 4, 5, 6],
                                             [7, 0, 4, -1, 0, -3], [0, 5, -6, 0, 0, 3],
                                             [1, 0, 3, 4, 5, 6], [0, 8, 0, 1, 2, 0],
                                             [-4, 0, 6, 0, 0, -5]])
        det = Matrix.calculate_det(test_matrix)
        self.assertEqual(det, -96)

if __name__ == "__main__":
    unittest.main(verbosity=2)

