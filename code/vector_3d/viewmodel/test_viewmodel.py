import unittest
import math

from vector_3d.viewmodel.viewmodel import Vector3dViewModel


class Vector3dViewModelTests(unittest.TestCase):
    def setUp(self):
        self.model = Vector3dViewModel()

    def test_norms_button_is_disabled_by_default(self):
        self.assertEqual('disabled', self.model.get_norms_button_state())

    def test_setting_norms_vector(self):
        self.model.set_norm_vector(1.0, 2.0, 3.0)
        self.assertAlmostEqual(1.0, self.model.get_vec0_x())
        self.assertAlmostEqual(2.0, self.model.get_vec0_y())
        self.assertAlmostEqual(3.0, self.model.get_vec0_z())

    def test_setting_norms_vector_enables_norms_button(self):
        self.model.set_norm_vector(1.0, 2.0, 3.0)
        self.assertEqual('normal', self.model.get_norms_button_state())

    def test_setting_norms_vector_with_incorrect_values_disables_norms_button(self):
        self.model.set_norm_vector('a', 'b', 'c')
        self.assertEqual('disabled', self.model.get_norms_button_state())

    def test_euclid_norm(self):
        x = 1.0
        y = 2.0
        z = 3.0
        self.model.set_norm_vector(x, y, z)
        self.model.calc_norms()
        result = math.sqrt(x * x + y * y + z * z)
        self.assertAlmostEqual(result, self.model.get_euclid_norm())

    def test_chebyshev_norm(self):
        x = 1.0
        y = 2.0
        z = 3.0
        self.model.set_norm_vector(x, y, z)
        self.model.calc_norms()
        result = max(abs(x), abs(y), abs(z))
        self.assertAlmostEqual(result, self.model.get_chebyshev_norm())

    def test_manhattan_norm(self):
        x = 1.0
        y = 2.0
        z = 3.0
        self.model.set_norm_vector(x, y, z)
        self.model.calc_norms()
        result = abs(x) + abs(y) + abs(z)
        self.assertAlmostEqual(result, self.model.get_manhattan_norm())

    def test_normalized_vector(self):
        self.model.set_norm_vector(1.0, 2.0, 3.0)
        self.model.calc_norms()
        result = [0.267, 0.534, 0.801]
        unit_vector = self.model.get_normalized_vector()
        for val1, val2 in zip(result, unit_vector):
            self.assertAlmostEqual(val1, val2, 2)

    def test_products_button_is_disabled_by_default(self):
        self.assertEqual('disabled', self.model.get_products_button_state())

    def test_setting_products_vectors(self):
        self.model.set_product_vectors(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        self.assertAlmostEqual(1.0, self.model.get_vec1_x())
        self.assertAlmostEqual(3.0, self.model.get_vec1_y())
        self.assertAlmostEqual(5.0, self.model.get_vec1_z())
        self.assertAlmostEqual(2.0, self.model.get_vec2_x())
        self.assertAlmostEqual(4.0, self.model.get_vec2_y())
        self.assertAlmostEqual(6.0, self.model.get_vec2_z())

    def test_setting_products_vectors_enables_products_button(self):
        self.model.set_product_vectors(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        self.assertEqual('normal', self.model.get_products_button_state())

    def test_setting_incorrect_products_vectors_disables_products_button(self):
        self.model.set_product_vectors(1.0, 2.0, 'a', 4.0, 'b', 'c')
        self.assertEqual('disabled', self.model.get_products_button_state())

    def test_dot_product(self):
        self.model.set_product_vectors(1.0, 1.0, 2.0, 2.0, 3.0, 3.0)
        self.model.calc_products()
        result = 14
        self.assertAlmostEqual(result, self.model.get_dot_product())

    def test_dot_product_with_negative_numbers(self):
        self.model.set_product_vectors(-1.0, -2.0, -3.0, -4.0, -5.0, -6.0)
        self.model.calc_products()
        result = 44
        self.assertAlmostEqual(result, self.model.get_dot_product())

    def test_cross_product(self):
        self.model.set_product_vectors(1.0, 3.0, 2.0, 2.0, 3.0, 1.0)
        self.model.calc_products()
        result = [-4.0, 8.0, -4.0]
        cross_product = self.model.get_cross_product()
        for val1, val2 in zip(result, cross_product):
            self.assertAlmostEqual(val1, val2)

    def test_cross_product_with_negative_numbers(self):
        self.model.set_product_vectors(-1.0, -2.0, -3.0, -4.0, -5.0, -6.0)
        self.model.calc_products()
        result = [-2.0, 4.0, -2.0]
        cross_product = self.model.get_cross_product()
        for val1, val2 in zip(result, cross_product):
            self.assertAlmostEqual(val1, val2)
