import unittest

from bisymmetric_matrix.viewmodel.viewmodel import BisymmetricMatrixViewModel


class TestBisymmetricMatrixCreate(unittest.TestCase):
    def test_create_view_model_object(self):
        view_model = BisymmetricMatrixViewModel()
        self.assertEqual(BisymmetricMatrixViewModel, type(view_model))

    def test_by_default_create_random_matrix_button_is_disabled(self):
        view_model = BisymmetricMatrixViewModel()
        self.assertEqual('disabled', view_model.is_create_random_matrix_button_enabled())

    def test_by_default_create_matrix_from_vector_button_is_disabled(self):
        view_model = BisymmetricMatrixViewModel()
        self.assertEqual('disabled', view_model.is_create_matrix_from_vector_button_enabled())

    def test_when_enter_vector_create_button_is_enabled(self):
        view_model = BisymmetricMatrixViewModel()
        view_model.get_vector([1, 2, 3])
        self.assertEqual('enabled', view_model.is_create_matrix_from_vector_button_enabled())

    def test_when_clear_vector_create_button_is_disabled(self):
        view_model = BisymmetricMatrixViewModel()
        view_model.get_vector([1, 2, 3])
        view_model.get_vector([])
        self.assertEqual('disabled', view_model.is_create_matrix_from_vector_button_enabled())
