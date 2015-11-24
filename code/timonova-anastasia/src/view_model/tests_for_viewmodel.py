import unittest

from view_model.viewmodel import ViewModel


class TestForViewModel(unittest.TestCase):
    def test_check_number_or_rows_in_init(self):
        view_model = ViewModel()
        self.assertEqual(view_model.get_number_of_rows(), 3)

    def test_check_init_matrix_by_zero_values(self):
        view_model = ViewModel()
        self.assertEqual(view_model.get_matrix_as_list(), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_check_int_matrix_by_non_zero_values(self):
        view_model = ViewModel()
        content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
        view_model.update_matrix_content(content)
        self.assertEqual(view_model.get_matrix_as_list(), [[2, 1, 2], [0, 3, 0], [3, 1, 1]])

    def test_get_number_of_rows(self):
        view_model = ViewModel()
        view_model.set_number_of_rows(4)
        self.assertEqual(view_model.get_number_of_rows(), 4)

    def test_change_matrix_rank(self):
        view_model = ViewModel()
        view_model.set_number_of_rows(4)
        print(view_model.init_zero_matrix_with_new_rank_value())
        self.assertEqual(view_model.init_zero_matrix_with_new_rank_value(), [[0, 0, 0, 0], [0, 0, 0, 0],
                                                                             [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_calculate_determinant(self):
        view_model = ViewModel()
        content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
        view_model.update_matrix_content(content)
        self.assertEqual(view_model.calculate_determinant(), -12)
