import unittest

from viewmodel import ViewModel


class TestForViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = ViewModel()

    def test_check_number_or_rows_in_init(self):
        self.assertEqual(self.view_model.get_number_of_rows(), 3)

    def test_check_init_matrix_by_zero_values(self):
        self.assertEqual(self.view_model.get_matrix_as_list(), [[0]*3]*3)

    def test_check_int_matrix_by_non_zero_values(self):
        content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
        self.view_model.update_matrix_content(content)
        self.assertEqual(self.view_model.get_matrix_as_list(), [[2, 1, 2], [0, 3, 0], [3, 1, 1]])

    def test_get_number_of_rows(self):
        self.view_model.set_number_of_rows(4)
        self.assertEqual(self.view_model.get_number_of_rows(), 4)

    def test_change_matrix_rank(self):
        self.view_model.set_number_of_rows(4)
        self.assertEqual(self.view_model.init_zero_matrix_with_new_rank_value(), [[0]*4]*4)

    def test_calculate_determinant(self):
        content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
        self.view_model.update_matrix_content(content)
        self.assertEqual(self.view_model.calculate_determinant(), -12)

    def test_set_answer(self):
        answer_str = '1'
        self.view_model.set_answer(answer_str)
        self.assertEqual(self.view_model.answer, answer_str)

    def test_check_correct_answer(self):
        content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
        self.view_model.update_matrix_content(content)
        self.view_model.calculate_determinant()
        self.assertEqual(self.view_model.answer, -12)
