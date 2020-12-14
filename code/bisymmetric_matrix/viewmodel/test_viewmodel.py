import unittest

from bisymmetric_matrix.viewmodel.viewmodel import BisymmetricMatrixViewModel


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
        self.assertEqual('1234', actual_vector)

    def test_when_enter_vector_clear_enter_invalid_vector_button_is_disabled(self):
        self.view_model.set_vector('1234')
        self.view_model.set_vector('1ert4')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_enter_vector_incorrect_size_button_is_disabled(self):
        self.view_model.set_vector('123')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_can_create_matrix_from_vector(self):
        self.view_model.set_vector('123456')
        self.view_model.create_matrix_from_vector()
        result = self.view_model.get_created_matrix_from_vector()
        correct_bisymmetric_matrix = '1234\n2563\n3652\n4321'
        for i in range(19):
            self.assertEqual(result[i], correct_bisymmetric_matrix[i])


class TestCreateRandomBisymmetricMatrix(unittest.TestCase):
    def setUp(self):
        self.view_model = BisymmetricMatrixViewModel()

    def test_by_default_create_random_matrix_is_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_choose_size_of_matrix_create_random_matrix_button_enabled(self):
        self.view_model.set_matrix_size('2x2')
        self.assertEqual('normal', self.view_model.get_button_convert_state())

    def test_when_select_2x2_size_of_create_matrix_is_2_rows_and_2_columns_plus_2_line_break(self):
        self.view_model.set_matrix_size('2x2')
        self.view_model.create_random_matrix()
        result = len(self.view_model.get_created_random_matrix())
        self.assertEqual(2*2+2, result)

    def test_when_select_3x3_size_of_create_matrix_is_3_rows_multi_3_columns_plus_3_line_break(self):
        self.view_model.set_matrix_size('3x3')
        self.view_model.create_random_matrix()
        result = len(self.view_model.get_created_random_matrix())
        self.assertEqual(3*3+3, result)

    def test_when_select_4x4_size_of_create_matrix_is_4_rows_multi_4_columns_plus_4_line_break(self):
        self.view_model.set_matrix_size('4x4')
        self.view_model.create_random_matrix()
        result = len(self.view_model.get_created_random_matrix())
        self.assertEqual(4*4+4, result)

    def test_when_select_5x5_size_of_create_matrix_is_5_rows_multi_5_columns_plus_5_line_break(self):
        self.view_model.set_matrix_size('5x5')
        self.view_model.create_random_matrix()
        result = len(self.view_model.get_created_random_matrix())
        self.assertEqual(5*5+5, result)

    def test_when_select_6x6_size_of_create_matrix_is_6_rows_multi_6_columns_plus_6_line_break(self):
        self.view_model.set_matrix_size('6x6')
        self.view_model.create_random_matrix()
        result = len(self.view_model.get_created_random_matrix())
        self.assertEqual(6*6+6, result)
