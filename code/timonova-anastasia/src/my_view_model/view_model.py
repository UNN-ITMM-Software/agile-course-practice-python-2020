from my_model.matrix import Matrix
from my_infrastructure.real_logger import RealLogger


class ViewError(Exception):
    pass


class ViewModel:
    def __init__(self, my_logger=RealLogger()):
        self.matrix = Matrix.make_from_list([[0]*3]*3)
        self.rows = 3
        self.answer = ''
        self.my_logger = my_logger  # RealLogger()
        self.my_logger.append_messages_in_logs_list('\n\n##    Start logging...    ##')

    def get_number_of_rows(self):
        self.my_logger.append_messages_in_logs_list('Getting matrix\'s rows: %s' % self.rows)
        return self.rows

    def set_number_of_rows(self, rows):
        self.rows = rows
        self.my_logger.append_messages_in_logs_list('Setting matrix\'s rows: %s' % self.rows)

    def get_matrix_as_list(self):
        self.my_logger.append_messages_in_logs_list('Getting matrix as data lines: %s' % self.matrix.get_data_lines())
        return self.matrix.get_data_lines()

    def set_answer(self, answer_str):
        self.answer = answer_str
        self.my_logger.append_messages_in_logs_list('Setting answer: %s' % self.answer)

    def update_matrix_content(self, content):
        self.matrix = Matrix.make_from_list(content)
        self.my_logger.append_messages_in_logs_list('Updating matrix\'s content: %s' % self.get_matrix_as_list())

    def calculate_determinant(self):
        self.answer = Matrix.calculate_det(self.matrix)
        self.my_logger.append_messages_in_logs_list('Calculating determinant: %s' % self.answer)
        return self.answer

    def init_zero_matrix_with_new_rank_value(self):
        self.matrix = Matrix.make_random(self.rows, self.rows, 0, 1)
        self.my_logger.append_messages_in_logs_list('Initialization zero matrix with new rank value.')
        return self.get_matrix_as_list()
