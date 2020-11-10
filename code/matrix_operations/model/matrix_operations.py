import random
import copy
from matrix.model.matrix import Matrix


class MatrixOperationsError(Exception):
    pass


class MatrixOperations(Matrix):
    def __init__(self, rows_count, cols_count):
        super().__init__(rows_count, cols_count)

    @classmethod
    def make_random(cls, rows_count, cols_count, min_value=0, max_value=10):
        my_matrix = MatrixOperations(rows_count, cols_count)
        for x in range(my_matrix.rows):
            my_matrix.data_lines.append([random.randrange(min_value, max_value)
                                         for y in range(my_matrix.cols)])
        return my_matrix

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
        if(first_matrix.rows == second_matrix.rows and first_matrix.cols == second_matrix.cols):
            return True
        return False

    @classmethod
    def add_matr(self, first_matrix, second_matrix):
        if not MatrixOperations.is_both_same_size(first_matrix, second_matrix):
            raise MatrixOperationsError('Matrices of different sizes! Check matrices elements.')
        return ([[elem1 + elem2 for elem1, elem2 in zip(row1, row2)] for row1, row2 in
                 zip(first_matrix.data_lines, second_matrix.data_lines)])


fm = MatrixOperations.make_from_list([[1, 1]])
sm = MatrixOperations.make_from_list([[-2, 0]])
# m = MatrixOperations.make_from_list(MatrixOperations.add_matr(fm, sm))
# print(m)
