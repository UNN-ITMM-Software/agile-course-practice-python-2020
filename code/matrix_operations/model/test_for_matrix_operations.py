import unittest

from matrix_operations.model.matrix_operations import MatrixOperations, MatrixOperationsError
from matrix.model.matrix import MatrixError


class TestMatrixOperationsClass(unittest.TestCase):

    def test_check_constructor(self):
        test_matrix = MatrixOperations.make_from_list([[1, 1]])
        self.assertTrue(test_matrix.cols == 2 and test_matrix.rows == 1 and test_matrix.data_lines[0][0] ==
                        test_matrix.data_lines[0][1] == 1)

    def test_plus_onesize_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 1]])
        second_matrix = MatrixOperations.make_from_list([[2, 2]])
        result_matrix = MatrixOperations.add_matrix(first_matrix, second_matrix)
        self.assertTrue(result_matrix.data_lines[0][0] == 3 and result_matrix.data_lines[0][1] == 3)

    def test_plus_onesize_negative_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 1]])
        second_matrix = MatrixOperations.make_from_list([[-2, 2]])
        result_matrix = MatrixOperations.add_matrix(first_matrix, second_matrix)
        self.assertTrue(result_matrix.data_lines[0][0] == -1 and result_matrix.data_lines[0][1] == 3)

    def test_plus_onesize_diff_char_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 1]])
        second_matrix = MatrixOperations.make_from_list([[-1, -1]])
        result_matrix = MatrixOperations.add_matrix(first_matrix, second_matrix)
        self.assertTrue(result_matrix.data_lines[0][0] == 0 and result_matrix.data_lines[0][1] == 0)

    def test_plus_3x2_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 1], [2, 2], [3, 3]])
        second_matrix = MatrixOperations.make_from_list([[-1, -1], [-1, -1], [-1, -1]])
        result_matrix = MatrixOperations.add_matrix(first_matrix, second_matrix)
        self.assertTrue(
            result_matrix.data_lines[0][0] == 0 and result_matrix.data_lines[1][1] == 1 and result_matrix.data_lines[2][
                1] == 2)

    def test_plus_diffsize_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 1]])
        second_matrix = MatrixOperations.make_from_list([[-1]])
        with self.assertRaises(MatrixOperationsError):
            MatrixOperations.add_matrix(first_matrix, second_matrix)

    def test_mult_square_2x2_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 0], [0, 1]])
        second_matrix = MatrixOperations.make_from_list([[3, 3], [3, 3]])
        result_matrix = MatrixOperations.multiply_matrix(first_matrix, second_matrix)
        self.assertTrue(result_matrix.data_lines[0][0] == 3 and result_matrix.data_lines[1][1] == 3)

    def test_mult_3x2_2x3_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 0], [0, 1], [1, 1]])
        second_matrix = MatrixOperations.make_from_list([[3, 3, 3], [3, 3, 3]])
        result_matrix = MatrixOperations.multiply_matrix(first_matrix, second_matrix)
        self.assertTrue(
            result_matrix.data_lines[0][0] == 3 and result_matrix.data_lines[1][1] == 3 and result_matrix.data_lines[2][
                2] == 6)

    def test_mult_3x2_2x2_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 0], [0, 1], [1, 1]])
        second_matrix = MatrixOperations.make_from_list([[3, 3], [3, 3]])
        result_matrix = MatrixOperations.multiply_matrix(first_matrix, second_matrix)
        self.assertTrue(
            result_matrix.data_lines[0][0] == 3 and result_matrix.data_lines[1][1] == 3 and result_matrix.data_lines[2][
                0] == 6)

    def test_mult_invalid_size_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 0], [0, 1], [1, 1]])
        second_matrix = MatrixOperations.make_from_list([[3, 3], [3, 3], [3, 3]])
        with self.assertRaises(MatrixOperationsError):
            MatrixOperations.multiply_matrix(first_matrix, second_matrix)

    def test_scalar_2_mult_square_2x2_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 2], [3, 4]])
        skalar = 2
        result_matrix = MatrixOperations.scalar_multiply_matrix(skalar, first_matrix)
        self.assertTrue(
            result_matrix.data_lines[0][0] == 2 and result_matrix.data_lines[1][1] == 8)

    def test_scalar_mult_3x2_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 2], [3, 4], [2, 2]])
        skalar = 2
        result_matrix = MatrixOperations.scalar_multiply_matrix(skalar, first_matrix)
        self.assertTrue(
            result_matrix.data_lines[0][0] == 2 and result_matrix.data_lines[1][1] == 8 and result_matrix.data_lines[2][
                1] == 4)

    def test_scalar_0_mult_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 2], [3, 4]])
        scalar = 0
        result_matrix = MatrixOperations.scalar_multiply_matrix(scalar, first_matrix)
        self.assertTrue(result_matrix == 0)

    def test_scalar_1_mult_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 2], [3, 4]])
        scalar = 1
        result_matrix = MatrixOperations.scalar_multiply_matrix(scalar, first_matrix)
        self.assertTrue(result_matrix.data_lines[0][0] == 1 and result_matrix.data_lines[1][1] == 4)

    def test_transpose_square_2x2_matrix(self):
        matrix = MatrixOperations.make_from_list([[1, 2], [3, 4]])
        result_matrix = MatrixOperations.transpose(matrix)
        self.assertTrue(result_matrix.data_lines[0][1] == 3 and result_matrix.data_lines[1][0] == 2)

    def test_transpose_3x2_matrix(self):
        matrix = MatrixOperations.make_from_list([[1, 2], [3, 4], [5, 6]])
        result_matrix = MatrixOperations.transpose(matrix)
        self.assertTrue(
            result_matrix.data_lines[0][1] == 3 and result_matrix.data_lines[1][0] == 2 and result_matrix.data_lines[0][
                2] == 5)

    def test_transpose_1x3_matrix(self):
        matrix = MatrixOperations.make_from_list([[1, 2, 3]])
        result_matrix = MatrixOperations.transpose(matrix)
        self.assertTrue(
            result_matrix.data_lines[0][0] == 1 and result_matrix.data_lines[1][0] == 2 and result_matrix.data_lines[2][
                0] == 3)

    def test_inverse_2x2_matrix(self):
        matrix = MatrixOperations.make_from_list([[1, 2], [3, 4]])
        result_matrix = MatrixOperations.inverse(matrix)
        self.assertTrue(
            result_matrix.data_lines[0][0] == -2 and result_matrix.data_lines[0][1] == 1 and
            result_matrix.data_lines[1][
                0] == 1.5 and result_matrix.data_lines[1][1] == -0.5)

    def test_inverse_invalid_size_matrix(self):
        matrix = MatrixOperations.make_from_list([[1, 2, 2], [3, 4, 4]])
        with self.assertRaises(MatrixError):
            MatrixOperations.inverse(matrix)

    def test_inverse_matrix_with_zero_det(self):
        matrix = MatrixOperations.make_from_list([[1, 2], [2, 4]])
        with self.assertRaises(MatrixError):
            MatrixOperations.inverse(matrix)
