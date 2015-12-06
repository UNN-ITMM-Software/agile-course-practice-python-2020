import unittest

from model.matrix import Matrix
from model.matrix import MatrixError


class MatrixTests(unittest.TestCase):

    def test_check_constructor(self):
        test_matrix = Matrix.make_from_list([[1, 1]])
        self.assertTrue(test_matrix.cols == 2 and test_matrix.rows == 1 and test_matrix.data_lines[0][0] ==
                        test_matrix.data_lines[0][1] == 1)

    def test_create_matrix_with_not_full_last_string(self):
        with self.assertRaises(MatrixError):
            Matrix.make_from_list([[1, 1, 1], [1, 1, 1], [1, 1]])

    def test_create_matrix_with_not_full_first_string(self):
        with self.assertRaises(MatrixError):
            Matrix.make_from_list([[1, 1], [1, 1, 1], [1, 2, 1]])

    def test_can_calculate_determinant_of_matrix1x1(self):
        test_matrix = Matrix.make_random(1, 1)
        det = test_matrix.calculate_det()
        self.assertTrue(test_matrix.data_lines[0][0] == det)

    def test_can_write_matrix_as_string(self):
        test_matrix = Matrix.make_from_list([[1, 3], [5, 7]])
        self.assertEqual(str(test_matrix), '1 3\n5 7\n')

    def test_check_exception(self):
        with self.assertRaises(MatrixError):
            test_matrix = Matrix.make_from_list([[1, 3]])
            test_matrix.calculate_det()

    def test_is_matrix_square(self):
        test_matrix = Matrix.make_random(3, 3)
        self.assertEqual(test_matrix.is_matrix_square(), True)

    def test_is_correct_index(self):
        test_matrix = Matrix.make_random(3, 3)
        self.assertEqual(test_matrix.is_correct_index(4, 3), False)

    def test_is_matrix_not_square(self):
        test_matrix = Matrix.make_random(3, 2)
        self.assertEqual(test_matrix.is_matrix_square(), 0)

    def test_can_not_delete_incorrect_col_or_row(self):
        test_matrix = Matrix.make_from_list([[1, 3], [5, 7], [5, 7]])
        with self.assertRaises(MatrixError):
            Matrix.delete_col_and_row(test_matrix, -100, -500)

    def test_can_calculate_determinant_of_matrix2x2(self):
        test_matrix = Matrix.make_from_list([[1, 3], [5, 7]])
        det = test_matrix.calculate_det()
        self.assertEqual(det, -8)

    def test_delete_zero_row_and_zero_col_in_matrix(self):
        test_matrix = Matrix.delete_col_and_row(
            Matrix.make_from_list([[1, 3], [5, 7]]), 0, 0)
        det = test_matrix.calculate_det()
        self.assertEqual(det, 7)

    def test_can_calculate_determinant_of_matrix3x3(self):
        test_matrix = Matrix.make_from_list([[7, 2, 0], [5, 8, 7], [1, 2, 3]])
        det = test_matrix.calculate_det()
        self.assertEqual(det, 54)

    def test_can_calculate_minor_0_1(self):
        test_matrix = Matrix.delete_col_and_row(
            Matrix.make_from_list([[1, 0, -3], [0, 0, 2], [-1, -2, 0]]), 0, 1)
        det = test_matrix.calculate_det()
        self.assertEqual(det, 2)

    def test_can_calculate_determinant_of_matrix6x6(self):
        test_matrix = Matrix.make_from_list([[-1, 2, 3, 4, 5, 6],
                                             [7, 0, 4, -1, 0, -3],
                                             [0, 5, -6, 0, 0, 3],
                                             [1, 0, 3, 4, 5, 6],
                                             [0, 8, 0, 1, 2, 0],
                                             [-4, 0, 6, 0, 0, -5]])
        det = test_matrix.calculate_det()
        self.assertEqual(det, -96)

    def test_get_data_line(self):
        test_matrix = Matrix.make_from_list([[7, 0], [5, 8]])
        self.assertEqual(test_matrix.get_data_lines(), [[7, 0], [5, 8]])
