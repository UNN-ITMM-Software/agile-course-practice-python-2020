import unittest

from bisymmetric_matrix.viewmodel.viewmodel import BisymmetricMatrixViewModel
from bisymmetric_matrix.logger.fakelogger import FakeLogger


class TestCreateBisymmetricMatrixFromVector(unittest.TestCase):
    def setUp(self):
        self.view_model = BisymmetricMatrixViewModel()

    def test_create_view_model_object(self):
        self.assertEqual(BisymmetricMatrixViewModel, type(self.view_model))

    def test_by_default_create_matrix_from_vector_is_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_enter_vector_create_matrix_from_vector_button_is_enabled(self):
        self.view_model.set_vector('1234')
        self.assertEqual('normal', self.view_model.get_button_convert_state())

    def test_when_delete_vector_create_matrix_from_vector_button_is_disabled(self):
        self.view_model.set_vector('1234')
        self.view_model.set_vector('')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_enter_letter_in_vector_button_is_disabled(self):
        self.view_model.set_vector('1f34')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_can_read_input_vector_text(self):
        self.view_model.set_vector('1234')
        actual_vector = self.view_model.get_input_vector()
        self.assertEqual([1, 2, 3, 4], actual_vector)

    def test_when_enter_vector_clear_enter_invalid_vector_button_is_disabled(self):
        self.view_model.set_vector('1234')
        self.view_model.set_vector('1ert4')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_enter_vector_incorrect_size_button_is_disabled(self):
        self.view_model.set_vector('123')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_can_create_matrix_from_vector(self):
        self.view_model.set_vector('123456')
        self.view_model.create_matrix_by_vector()
        result = self.view_model.get_str_created_matrix_by_vector()
        correct_bisymmetric_matrix = ' 1 2 3 4\n 2 5 6 3\n 3 6 5 2\n 4 3 2 1\n'
        for i in range(36):
            self.assertEqual(result[i], correct_bisymmetric_matrix[i])


class TestCreateRandomBisymmetricMatrix(unittest.TestCase):
    def setUp(self):
        self.view_model = BisymmetricMatrixViewModel()

    def test_by_default_create_random_matrix_is_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_choose_size_of_matrix_create_random_matrix_button_enabled(self):
        self.view_model.set_matrix_size('2')
        self.assertEqual('normal', self.view_model.get_button_convert_state())

    def test_when_select_size_2_create_matrix_size_is_correct(self):
        self.view_model.set_matrix_size('2')
        self.view_model.create_random_matrix()
        result = len(self.view_model.get_str_created_random_matrix())
        self.assertEqual((2+2)*2+2, result)

    def test_when_enter_size_clear_enter_invalid_size_button_is_disabled(self):
        self.view_model.set_matrix_size('2')
        self.view_model.set_matrix_size('e3')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_delete_vector_create_matrix_from_vector_button_is_disabled(self):
        self.view_model.set_matrix_size('3')
        self.view_model.set_matrix_size('')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())


class TestAdditionalMethod(unittest.TestCase):
    def setUp(self):
        self.view_model = BisymmetricMatrixViewModel()

    def test_convert_vector_str_to_vector_list(self):
        vector_str = '1234'
        self.assertEqual([1, 2, 3, 4], self.view_model.convert_str_to_vector(vector_str))

    def test_convert_matrix_list_to_matrix_str(self):
        matrix = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
        result = ' 1 2 3\n 2 3 4\n 5 6 7\n'
        self.view_model.matrix_size = 3
        for i in range(21):
            self.assertEqual(self.view_model.convert_random_matrix_to_str(matrix)[i], result[i])


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = BisymmetricMatrixViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome', self.view_model.logger.get_last_message())

    def test_logging_changing_first_fraction(self):
        matrix = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
        self.view_model.set_created_random_matrix(matrix)
        result = self.view_model.convert_random_matrix_to_str(matrix)
        self.assertEqual(result, self.view_model.logger.get_last_message())

    def test_logging_changing_first_fraction_2(self):
        matrix = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
        self.view_model.set_created_matrix_by_vector(matrix)
        result = self.view_model.convert_random_matrix_to_str(matrix)
        self.assertEqual(result, self.view_model.logger.get_last_message())

    def test_logging_all(self):
        matrix = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
        self.view_model.set_created_matrix_by_vector(matrix)
        result1 = self.view_model.convert_random_matrix_to_str(matrix)
        matrix2 = [[12, 2, 3], [2, 3, 4], [5, 6, 7]]
        self.view_model.set_created_random_matrix(matrix2)
        result2 = self.view_model.convert_random_matrix_to_str(matrix2)
        all_res = ['Welcome', result1, result2]
        self.assertEqual(all_res, self.view_model.logger.get_log_messages())
