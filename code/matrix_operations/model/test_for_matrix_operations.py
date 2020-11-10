import unittest

from matrix_operations.model.matrix_operations import MatrixOperations, MatrixOperationsError

class TestMatrixOperationsClass(unittest.TestCase):

    def test_check_constructor(self):
        test_matrix = MatrixOperations.make_from_list([[1, 1]])
        self.assertTrue(test_matrix.cols == 2 and test_matrix.rows == 1 and test_matrix.data_lines[0][0] ==
                        test_matrix.data_lines[0][1] == 1)

    def test_plus_onesize_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1,1]])
        second_matrix = MatrixOperations.make_from_list([[2,2]])
        result_matrix = MatrixOperations.make_from_list(MatrixOperations.add_matr(first_matrix, second_matrix))
        self.assertTrue(result_matrix.data_lines[0][0] == 3 and result_matrix.data_lines[0][1]==3)

    def test_plus_onesize_negative_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 1]])
        second_matrix = MatrixOperations.make_from_list([[-2, 2]])
        result_matrix = MatrixOperations.make_from_list(MatrixOperations.add_matr(first_matrix, second_matrix))
        self.assertTrue(result_matrix.data_lines[0][0] == -1 and result_matrix.data_lines[0][1] == 3)

    def test_plus_onesize_diff_char_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 1]])
        second_matrix = MatrixOperations.make_from_list([[-1, -1]])
        result_matrix = MatrixOperations.make_from_list(MatrixOperations.add_matr(first_matrix, second_matrix))
        self.assertTrue(result_matrix.data_lines[0][0] == 0 and result_matrix.data_lines[0][1] == 0)

    def test_plus_diffsize_matrix(self):
        first_matrix = MatrixOperations.make_from_list([[1, 1]])
        second_matrix = MatrixOperations.make_from_list([[-1]])
        with self.assertRaises(MatrixOperationsError):
            MatrixOperations.add_matr(first_matrix, second_matrix)