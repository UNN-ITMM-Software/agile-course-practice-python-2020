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
        self.view_model.set_vector([1, 2, 3])
        self.assertEqual('normal', self.view_model.get_button_convert_state())

    def test_when_delete_vector_create_matrix_from_vector_button_is_disabled(self):
        self.view_model.set_vector('1, 2, 3')
        self.view_model.set_vector('')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())


class TestCreateRandomBisymmetricMatrix(unittest.TestCase):
    def setUp(self):
        self.view_model = BisymmetricMatrixViewModel()

    def test_by_default_create_random_matrix_is_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_choose_size_of_matrix_create_random_matrix_button_enabled(self):
        self.view_model.set_matrix_size('2x2')
        self.assertEqual('normal', self.view_model.get_button_convert_state())
