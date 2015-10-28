import random
import copy


class MatrixError(Exception):
    """ An exception class for Matrix """
    pass


class Matrix(object):
    """ matrix class with some basis func. """
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
        """ Calculate determinant of matrix """
        if self.rows == 1 and self.cols == 1:
            return self.data_lines[0][0]
        elif self.rows == 2 and self.cols == 2:
            return self.data_lines[0][0] * self.data_lines[1][1] - \
                self.data_lines[1][0] * self.data_lines[0][1]
        else:
            determinant = 0
            if self.is_matrix_square() < 1:
                raise MatrixError('Matrix must be square!')
            for i in range(0, self.rows):
                sub_matrix = Matrix.del_col_and_row(self, i, 0)
                sub_det = Matrix.calculate_det(sub_matrix)
                determinant += (-1) ** (i + 2) *\
                    self.data_lines[i][0] * sub_det
        return determinant

    @classmethod
    def make_random(cls, rows_count, cols_count, low_number_limit=0,
                    high_number_limit=10):
        """ Make a random matrix with elements in range (low-high) """
        obj = Matrix(rows_count, cols_count)
        for x in range(obj.rows):
            obj.data_lines.append([random.randrange(low_number_limit,
                                                    high_number_limit)
                                   for y in range(obj.cols)])
        return obj

    @classmethod
    def make_from_list(cls, input_data_list):
        """ Create a matrix from list """
        data_lines = input_data_list[:]
        return cls.make_matrix(data_lines)

    @classmethod
    def make_matrix(cls, data_lines):

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
