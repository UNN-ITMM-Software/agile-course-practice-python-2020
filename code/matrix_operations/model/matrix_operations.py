import random
from matrix.model.matrix import Matrix
from matrix.model.matrix import MatrixError


class MatrixOperationsError(Exception):
    pass


class MatrixOperations(Matrix):
    def __init__(self, rows_count, cols_count):
        super().__init__(rows_count, cols_count)

    @classmethod
    def make_from_list(cls, input_data_list):
        my_rows = len(input_data_list[:])
        my_cols = 0
        for i in range(0, my_rows):
            if len(input_data_list[:][i]) > my_cols:
                my_cols = len(input_data_list[:][i])
        if not Matrix.is_full_matrix(input_data_list):
            raise MatrixOperationsError('Matrix isn\'t  full! Check matrix elements.')
        my_matrix = MatrixOperations(my_rows, my_cols)
        my_matrix.data_lines = input_data_list[:]
        return my_matrix

    @classmethod
    def is_both_same_size(cls, first_matrix, second_matrix):
        if (first_matrix.rows == second_matrix.rows and first_matrix.cols == second_matrix.cols):
            return True
        return False

    @classmethod
    def add_matrix(cls, first_matrix, second_matrix):
        if not MatrixOperations.is_both_same_size(first_matrix, second_matrix):
            raise MatrixOperationsError('Matrices of different sizes! Check matrices elements.')
        return MatrixOperations.make_from_list([[elem1 + elem2 for elem1, elem2 in zip(row1, row2)]
                                                for row1, row2 in
                                                zip(first_matrix.data_lines, second_matrix.data_lines)])

    @classmethod
    def can_multiply_matrix(cls, first_matrix, second_matrix):
        if first_matrix.cols == second_matrix.rows:
            return True
        return False

    @classmethod
    def multiply_matrix(cls, first_matrix, second_matrix):
        if not MatrixOperations.can_multiply_matrix(first_matrix, second_matrix):
            raise MatrixOperationsError('Matrices has invalid sizes! Check matrices size.')
        result_matrix = MatrixOperations.make_from_list(
            [[0 for i in range(second_matrix.cols)] for i in range(first_matrix.rows)])
        for i in range(first_matrix.rows):
            for j in range(second_matrix.cols):
                for k in range(first_matrix.cols):
                    result_matrix.data_lines[i][j] += first_matrix.data_lines[i][k] * \
                                                      second_matrix.data_lines[k][j]
        return result_matrix

    @classmethod
    def scalar_multiply_matrix(cls, scalar, matrix):
        if scalar == 0:
            return 0
        elif scalar == 1:
            return matrix
        return MatrixOperations.make_from_list([[scalar * elem for elem in row] for row in matrix.data_lines])

    @classmethod
    def transpose(cls, matrix):
        return MatrixOperations.make_from_list([list(row) for row in zip(*matrix.data_lines)])

    @classmethod
    def inverse(cls, matrix):
        if matrix.calculate_det() == 0:
            raise MatrixError('Matrix has zero determinant! Check your matrix.')
        minor_matrix = MatrixOperations.make_from_list(
            [[0 for i in range(matrix.cols)] for i in range(matrix.rows)])
        for i in range(minor_matrix.rows):
            for j in range(minor_matrix.cols):
                minor = MatrixOperations.delete_col_and_row(matrix, i, j)
                minor_matrix.data_lines[i][j] = minor.calculate_det() * ((-1) ** (i + j))
        minor_matrix = MatrixOperations.transpose(minor_matrix)
        return MatrixOperations.make_from_list(
            [[elem / matrix.calculate_det() for elem in row] for row in minor_matrix.data_lines])
