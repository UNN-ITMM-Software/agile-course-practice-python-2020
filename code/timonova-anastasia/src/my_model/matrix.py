import random
import copy


class MatrixError(Exception):
    pass


class Matrix(object):
    def __init__(self, rows_count, cols_count):
        self.rows = rows_count
        self.cols = cols_count
        self.data_lines = []

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row])
                       for row in self.data_lines])
        return s + '\n'

    def get_data_lines(self):
        return self.data_lines

    def is_matrix_square(self):
        return True if self.rows == self.cols else False

    @classmethod
    def is_full_matrix(cls, input_data_list):
        for i in range(1, len(input_data_list)):
            if len(input_data_list[i]) != len(input_data_list[0]):
                return False
        return True

    def is_correct_index(self, row, col):
        return True if 0 <= row < self.rows and 0 <= col < self.cols\
            else False

    def calculate_det(self):
        if not self.is_matrix_square():
            raise MatrixError('Matrix must be square!')
        else:
            if self.rows == 1:
                return self.data_lines[0][0]
            elif self.rows == 2:
                return self.data_lines[0][0] * self.data_lines[1][1] - \
                    self.data_lines[1][0] * self.data_lines[0][1]
            else:
                determinant = 0
                for i in range(0, self.rows):
                    sub_matrix = Matrix.delete_col_and_row(self, i, 0)
                    sub_det = sub_matrix.calculate_det()
                    determinant += (-1) ** (i + 2) *\
                        self.data_lines[i][0] * sub_det
        return determinant

    @classmethod
    def make_random(cls, rows_count, cols_count, min_value=0,
                    max_value=10):
        my_matrix = Matrix(rows_count, cols_count)
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
            raise MatrixError('Matrix isn\'t  full! Check matrix elements.')
        my_matrix = Matrix(my_rows, my_cols)
        my_matrix.data_lines = input_data_list[:]
        return my_matrix

    @classmethod
    def delete_col_and_row(cls, matrix, del_row, del_col):
        if not matrix.is_correct_index(del_row, del_col):
            raise MatrixError('Row or col index out of range!')
        new_matrix = copy.deepcopy(matrix)
        del new_matrix.data_lines[del_row]
        for i in range(0, new_matrix.rows - 1):
            del new_matrix.data_lines[i][del_col]
        new_matrix.rows -= 1
        new_matrix.cols -= 1
        return new_matrix
