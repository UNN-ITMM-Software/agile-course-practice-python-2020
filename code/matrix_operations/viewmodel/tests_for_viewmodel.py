import unittest

from matrix_operations.viewmodel.viewmodel import MatrixOperationsViewModel


class TestFractionCalculatorViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = MatrixOperationsViewModel()

    def test_get_number_of_rows(self):
        self.assertEqual(self.view_model.get_number_of_rows(), 3)

    def test_get_matrix1_as_list(self):
        content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
        self.view_model.update_matrix1_content(content)
        self.assertEqual(self.view_model.get_matrix1_as_list(), [[2, 1, 2], [0, 3, 0], [3, 1, 1]])

    def test_get_matrix2_as_list(self):
        content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
        self.view_model.update_matrix2_content(content)
        self.assertEqual(self.view_model.get_matrix2_as_list(), [[2, 1, 2], [0, 3, 0], [3, 1, 1]])

    def test_calculate_determinant1(self):
        content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
        self.view_model.update_matrix1_content(content)
        self.assertEqual(self.view_model.calculate_determinant1(), -12)

    def test_calculate_determinant2(self):
        content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
        self.view_model.update_matrix2_content(content)
        self.assertEqual(self.view_model.calculate_determinant2(), -12)

    def test_transpose1(self):
        content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
        self.view_model.update_matrix1_content(content)
        self.assertEqual(self.view_model.transpose1(), [[2, 0, 3], [1, 3, 1], [2, 0, 1]])

    def test_transpose2(self):
        content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
        self.view_model.update_matrix2_content(content)
        self.assertEqual(self.view_model.transpose2(), [[2, 0, 3], [1, 3, 1], [2, 0, 1]])

    def test_inverse1(self):
        content = [[1, 0, 0], [0, 2, 0], [0, 0, 4]]
        self.view_model.update_matrix1_content(content)
        self.assertEqual(self.view_model.inverse1(), [[1, 0, 0], [0, 0.5, 0], [0, 0, 0.25]])

    def test_inverse2(self):
        content = [[1, 0, 0], [0, 2, 0], [0, 0, 4]]
        self.view_model.update_matrix2_content(content)
        self.assertEqual(self.view_model.inverse2(), [[1, 0, 0], [0, 0.5, 0], [0, 0, 0.25]])

    def test_sum(self):
        content1 = [[1, 0, 0], [0, 2, 0], [0, 0, 4]]
        self.view_model.update_matrix1_content(content1)
        content2 = [[1, 0, 0], [0, 3, 0], [0, 0, 7]]
        self.view_model.update_matrix2_content(content2)
        self.assertEqual(self.view_model.sum(), [[2, 0, 0], [0, 5, 0], [0, 0, 11]])

    def test_mul(self):
        content1 = [[1, 0, 0], [0, 2, 0], [0, 0, 4]]
        self.view_model.update_matrix1_content(content1)
        content2 = [[1, 0, 0], [0, 3, 0], [0, 0, 7]]
        self.view_model.update_matrix2_content(content2)
        self.assertEqual(self.view_model.mul(), [[1, 0, 0], [0, 6, 0], [0, 0, 28]])

    def test_calculate_from_set(self):
        self.view_model.set_operation('Transpose1')
        content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
        self.view_model.update_matrix1_content(content)
        self.assertEqual(self.view_model.calculate(), [[2, 0, 3], [1, 3, 1], [2, 0, 1]])
