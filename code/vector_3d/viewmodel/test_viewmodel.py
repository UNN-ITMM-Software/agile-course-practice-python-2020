import unittest
import math

from vector_3d.viewmodel.viewmodel import Vector3dViewModel
from vector_3d.infrastructure.fake_logger import FakeLogger
from vector_3d.infrastructure.real_logger import RealLogger


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


class TestVector3dViewModelFakeLogger(unittest.TestCase):
    def setUp(self):
        self.model = Vector3dViewModel(FakeLogger())

    def test_log_init(self):
        self.assertEqual('Logging', self.model.logger.get_last_message())

    def test_norms_button_is_disabled_by_default(self):
        self.model.get_norms_button_state()
        self.assertEqual('Norm button state: {}'.format(self.model.button_norms), self.model.logger.get_last_message())

    def test_setting_norms_vector_enables_norms_button(self):
        self.model.set_norm_vector(1.0, 2.0, 3.0)
        self.model.get_norms_button_state()
        self.assertEqual('Norm button state: {}'.format(self.model.button_norms), self.model.logger.get_last_message())

    def test_setting_norms_vector_with_incorrect_values_disables_norms_button(self):
        self.model.set_norm_vector('a', 'b', 'c')
        self.model.get_norms_button_state()
        self.assertEqual('Norm button state: {}'.format(self.model.button_norms), self.model.logger.get_last_message())

    def test_set_norm_vector(self):
        self.model.set_norm_vector(1.0, 2.0, 3.0)
        self.assertEqual(['Logging', 'Set norm vector: x = {0}, y = {1}, z = {2}'.format(1.0, 2.0, 3.0),
                          'Norm vector coordinates: x = {0}, y = {1}, z = {2}'.format(self.model.norm_vector.x,
                                                                                      self.model.norm_vector.y,
                                                                                      self.model.norm_vector.z)],
                         self.model.logger.get_log_messages())

    def test_coordinates_norm_vector(self):
        self.model.set_norm_vector(1.0, 2.0, 3.0)
        self.model.get_vec0_x()
        self.model.get_vec0_y()
        self.model.get_vec0_z()
        self.assertEqual(['Norm vector coordinate x = {}'.format(self.model.vec0_x),
                          'Norm vector coordinate y = {}'.format(self.model.vec0_y),
                          'Norm vector coordinate z = {}'.format(self.model.vec0_z)],
                         self.model.logger.get_several_messages(3))

    def test_products_button_is_disabled_by_default(self):
        self.model.get_products_button_state()
        self.assertEqual('Product button state: {}'.format(self.model.button_products),
                         self.model.logger.get_last_message())

    def test_setting_products_vectors_enables_products_button(self):
        self.model.set_product_vectors(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        self.model.get_products_button_state()
        self.assertEqual('Product button state: {}'.format(self.model.button_products),
                         self.model.logger.get_last_message())

    def test_setting_incorrect_products_vectors_disables_products_button(self):
        self.model.set_product_vectors(1.0, 2.0, 'a', 4.0, 'b', 'c')
        self.model.get_products_button_state()
        self.assertEqual('Product button state: {}'.format(self.model.button_products),
                         self.model.logger.get_last_message())

    def test_set_product_vectors(self):
        self.model.set_product_vectors(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        self.assertEqual(['Logging', 'Set product vectors: x1 = {0}, y1 = {1}, z1 = {2},'
                                     ' x2 = {3}, y2 = {4}, z2 = {5}'.format(1.0, 3.0, 5.0, 2.0, 4.0, 6.0),
                          'First product vector: x = {0}, y = {1}, z = {2},'
                          ' Second product vector: x = {0}, y = {1}, z = {2},'.format(self.model.first_vector.x,
                                                                                      self.model.first_vector.y,
                                                                                      self.model.first_vector.z,
                                                                                      self.model.second_vector.x,
                                                                                      self.model.second_vector.y,
                                                                                      self.model.second_vector.z)],
                         self.model.logger.get_log_messages())

    def test_coordinates_first_product_vector(self):
        self.model.set_product_vectors(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        self.model.get_vec1_x()
        self.model.get_vec1_y()
        self.model.get_vec1_z()
        self.assertEqual(['First product vector coordinate x = {}'.format(self.model.vec1_x),
                          'First product vector coordinate y = {}'.format(self.model.vec1_y),
                          'First product vector coordinate z = {}'.format(self.model.vec1_z)],
                         self.model.logger.get_several_messages(3))

    def test_coordinates_second_product_vector(self):
        self.model.set_product_vectors(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        self.model.get_vec2_x()
        self.model.get_vec2_y()
        self.model.get_vec2_z()
        self.assertEqual(['Second product vector coordinate x = {}'.format(self.model.vec2_x),
                          'Second product vector coordinate y = {}'.format(self.model.vec2_y),
                          'Second product vector coordinate z = {}'.format(self.model.vec2_z)],
                         self.model.logger.get_several_messages(3))

    def test_calc_all_norms(self):
        x = 1.0
        y = 2.0
        z = 3.0
        self.model.set_norm_vector(x, y, z)
        self.model.calc_norms()
        self.assertEqual(['Calculate Euclid norm: {}'.format(self.model.euclid_norm),
                          'Calculate Manhattan norm: {}'.format(self.model.manhattan_norm),
                          'Calculate Chebyshev norm: {}'.format(self.model.chebyshev_norm),
                          'Calculate normalized vector: {}'.format(self.model.normalized_vector)],
                         self.model.logger.get_several_messages(4))

    def test_euclid_norm(self):
        x = 1.0
        y = 2.0
        z = 3.0
        self.model.set_norm_vector(x, y, z)
        self.model.get_euclid_norm()
        self.assertEqual('Euclid norm: {}'.format(self.model.euclid_norm), self.model.logger.get_last_message())

    def test_manhattan_norm(self):
        x = 1.0
        y = 2.0
        z = 3.0
        self.model.set_norm_vector(x, y, z)
        self.model.get_manhattan_norm()
        self.assertEqual('Manhattan norm: {}'.format(self.model.manhattan_norm), self.model.logger.get_last_message())

    def test_chebyshev_norm(self):
        x = 1.0
        y = 2.0
        z = 3.0
        self.model.set_norm_vector(x, y, z)
        self.model.get_chebyshev_norm()
        self.assertEqual('Chebyshev norm: {}'.format(self.model.chebyshev_norm), self.model.logger.get_last_message())

    def test_normalized_vector(self):
        x = 1.0
        y = 2.0
        z = 3.0
        self.model.set_norm_vector(x, y, z)
        self.model.get_normalized_vector()
        self.assertEqual('Normalized vector: {}'.format(self.model.normalized_vector),
                         self.model.logger.get_last_message())

    def test_all_product(self):
        self.model.set_product_vectors(1.0, 1.0, 2.0, 2.0, 3.0, 3.0)
        self.model.calc_products()
        self.assertEqual(['Calculate dot product: {}'.format(self.model.dot_product),
                          'Calculate cross product: {}'.format(self.model.cross_product)],
                         self.model.logger.get_several_messages(2))

    def test_dot_product(self):
        self.model.set_product_vectors(1.0, 1.0, 2.0, 2.0, 3.0, 3.0)
        self.model.get_dot_product()
        self.assertEqual('Dot product: {}'.format(self.model.dot_product),
                         self.model.logger.get_last_message())

    def test_cross_product(self):
        self.model.set_product_vectors(1.0, 1.0, 2.0, 2.0, 3.0, 3.0)
        self.model.get_cross_product()
        self.assertEqual('Cross product: {}'.format(self.model.cross_product),
                         self.model.logger.get_last_message())


class TestVector3dViewModelRealLogger(TestVector3dViewModelFakeLogger):
    def setUp(self):
        self.model = Vector3dViewModel(RealLogger())
