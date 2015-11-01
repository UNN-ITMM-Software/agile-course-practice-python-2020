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

    def is_matrix_square(self):
        if self.rows == self.cols:
            return True
        return False

    def calculate_det(self):
        if self.is_matrix_square() is False:
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
        data_lines = input_data_list[:]
        m = len(data_lines)
        n = len(data_lines[0])
        my_matrix = Matrix(m, n)
        my_matrix.data_lines = data_lines
        return my_matrix

    @classmethod
    def delete_col_and_row(cls, matrix, del_row, del_col):
        new_matrix = copy.deepcopy(matrix)
        del new_matrix.data_lines[del_row]
        for i in range(0, new_matrix.rows - 1):
            del new_matrix.data_lines[i][del_col]
        new_matrix.rows -= 1
        new_matrix.cols -= 1
        return new_matrix
