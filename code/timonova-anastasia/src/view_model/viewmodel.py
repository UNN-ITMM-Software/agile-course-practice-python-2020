from model.matrix import Matrix


class ViewError(Exception):
    pass


class ViewModel():
    def __init__(self):
        self.matrix = Matrix.make_from_list([[0]*3]*3)
        self.rows = 3
        self.answer = ''

    def get_number_of_rows(self):
        return self.rows

    def set_number_of_rows(self, rows):
        self.rows = rows

    def get_matrix_as_list(self):
        return self.matrix.get_data_lines()

    def set_answer(self, answer_str):
        self.answer = answer_str

    def update_matrix_content(self, content):
        self.matrix = Matrix.make_from_list(content)

    def calculate_determinant(self):
        self.answer = Matrix.calculate_det(self.matrix)
        return self.answer

    def init_zero_matrix_with_new_rank_value(self):
        self.matrix = Matrix.make_random(self.rows, self.rows, 0, 1)
        return self.get_matrix_as_list()
