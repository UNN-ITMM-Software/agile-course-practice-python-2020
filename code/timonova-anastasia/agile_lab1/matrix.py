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
            return 1
        return 0

    def calculate_det(self):
        if self.is_matrix_square() > 0:
            if self.rows == 1:
                return self.data_lines[0][0]
            elif self.rows == 2:
                return self.data_lines[0][0] * self.data_lines[1][1] - \
                    self.data_lines[1][0] * self.data_lines[0][1]
            else:
                determinant = 0
                if self.is_matrix_square() < 1:
                    raise MatrixError('Matrix must be square!')
                for i in range(0, self.rows):
                    sub_matrix = Matrix.del_col_and_row(self, i, 0)
                    sub_det = sub_matrix.calculate_det()
                    determinant += (-1) ** (i + 2) *\
                        self.data_lines[i][0] * sub_det
        else:
            raise MatrixError('Matrix must be square!')
        return determinant

    @classmethod
    def make_random(cls, rows_count, cols_count, low_number_limit=0,
                    high_number_limit=10):
        obj = Matrix(rows_count, cols_count)
        for x in range(obj.rows):
            obj.data_lines.append([random.randrange(low_number_limit,
                                                    high_number_limit)
                                   for y in range(obj.cols)])
        return obj

    @classmethod
    def make_from_list(cls, input_data_list):
        data_lines = input_data_list[:]
        m = len(data_lines)
        n = len(data_lines[0])
        mat = Matrix(m, n)
        mat.data_lines = data_lines
        return mat

    @classmethod
    def del_col_and_row(cls, matrix, del_row, del_col):
        new_matrix = copy.deepcopy(matrix)
        del new_matrix.data_lines[del_row]
        for i in range(0, new_matrix.rows - 1):
            del new_matrix.data_lines[i][del_col]
        new_matrix.rows -= 1
        new_matrix.cols -= 1
        return new_matrix
