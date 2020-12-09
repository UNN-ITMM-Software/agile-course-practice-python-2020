import unittest
from vector_3d.model.vector_3d import Vector3d


class TestVector3d(unittest.TestCase):

    def test_can_create_vector(self):
        vec = Vector3d()
        self.assertTrue(isinstance(vec, Vector3d))

    def test_can_create_1_2_3_vector(self):
        vec = Vector3d(1, 2, 3)
        self.assertTrue(vec.is_equal(1.0, 2.0, 3.0))

    def test_can_not_create_1_2_3_vector(self):
        vec = Vector3d(1, 2, 3)
        self.assertTrue(not vec.is_equal(1.1, 2.1, 3.1))

    def test_calc_euclid_norma_1_3_4(self):
        vec = Vector3d(1.0, 3.0, 4.0)
        norma = vec.calc_norma()
        self.assertAlmostEqual(norma, 5, 0)

    def test_calc_euclid_norma_3_4_5(self):
        vec = Vector3d(3.0, 4.0, 5.0)
        norma = vec.calc_norma()
        self.assertAlmostEqual(norma, 7.07, 2)

    def test_calc_euclid_norma_negative_numbers(self):
        vec = Vector3d(-3.3, 2.0, -4.8)
        norma = vec.calc_norma()
        self.assertAlmostEqual(norma, 6.15873, 4)

    def test_calc_euclid_norma_zeros(self):
        vec = Vector3d(0.0, 0.0, 0.0)
        norma = vec.calc_norma()
        self.assertAlmostEqual(norma, 0, 0)

    def test_calc_manhattan_norma_1_3_4(self):
        vec = Vector3d(1.0, 3.0, 4.0)
        norma = vec.calc_norma(norma_type='manhattan')
        self.assertAlmostEqual(norma, 8, 0)

    def test_calc_manhattan_norma_3_4_5(self):
        vec = Vector3d(3.0, 4.0, 5.0)
        norma = vec.calc_norma(norma_type='manhattan')
        self.assertAlmostEqual(norma, 12, 0)

    def test_calc_manhattan_norma_negative_numbers(self):
        vec = Vector3d(-3.3, 2.0, -4.8)
        norma = vec.calc_norma(norma_type='manhattan')
        self.assertAlmostEqual(norma, 10.1, 1)

    def test_calc_manhattan_norma_zeros(self):
        vec = Vector3d(0.0, 0.0, 0.0)
        norma = vec.calc_norma(norma_type='manhattan')
        self.assertAlmostEqual(norma, 0, 0)

    def test_calc_chebyshev_norma_1_3_4(self):
        vec = Vector3d(1.0, 3.0, 4.0)
        norma = vec.calc_norma(norma_type='chebyshev')
        self.assertAlmostEqual(norma, 4, 0)

    def test_calc_chebyshev_norma_x_max(self):
        vec = Vector3d(-40.0, 20.0, -24.0)
        norma = vec.calc_norma(norma_type='chebyshev')
        self.assertAlmostEqual(norma, 40, 0)

    def test_calc_chebyshev_norma_y_max(self):
        vec = Vector3d(-4.0, 20.0, -14.0)
        norma = vec.calc_norma(norma_type='chebyshev')
        self.assertAlmostEqual(norma, 20, 0)

    def test_calc_chebyshev_norma_z_max(self):
        vec = Vector3d(-4.0, 20.0, -34.0)
        norma = vec.calc_norma(norma_type='chebyshev')
        self.assertAlmostEqual(norma, 34, 0)

    def test_calc_chebyshev_norma_zeros(self):
        vec = Vector3d(0.0, 0.0, 0.0)
        norma = vec.calc_norma(norma_type='chebyshev')
        self.assertAlmostEqual(norma, 0, 0)

    def test_calc_does_not_exist_type(self):
        vec = Vector3d(1.0, 3.0, 4.0)
        with self.assertWarnsRegex(Warning, "Error! Input type doesn't exist."):
            norma = vec.calc_norma(norma_type='not type')
        self.assertAlmostEqual(norma, 0, 0)

    def test_calc_normalization_1_3_4(self):
        vec = Vector3d(1.0, 3.0, 4.0)
        normalization = vec.calc_normalization()
        vec_params = [0.196, 0.588, 0.784]
        for val1, val2 in zip(normalization, vec_params):
            self.assertAlmostEqual(val1, val2, 3)

    def test_calc_normalization_3_4_5(self):
        vec = Vector3d(3.0, 4.0, 5.0)
        normalization = vec.calc_normalization()
        vec_params = [0.424, 0.5656, 0.707]
        for val1, val2 in zip(normalization, vec_params):
            self.assertAlmostEqual(val1, val2, 3)

    def test_calc_normalization_negative_numbers(self):
        vec = Vector3d(-3.3, 2.0, -4.8)
        normalization = vec.calc_normalization()
        vec_params = [-0.5358, 0.3247, -0.7793]
        for val1, val2 in zip(normalization, vec_params):
            self.assertAlmostEqual(val1, val2, 3)

    def test_calc_normalization_zero(self):
        vec = Vector3d(0, 0, 0)
        with self.assertWarnsRegex(Warning, 'Error! Division by zero.'):
            normalization = vec.calc_normalization()
        vec_params = [0.0, 0.0, 0.0]
        for val1, val2 in zip(normalization, vec_params):
            self.assertAlmostEqual(val1, val2, 0)

    def test_calc_simple_scalar_product(self):
        vec1 = Vector3d(1.0, 2.0, 3.0)
        vec2 = Vector3d(3.0, 2.0, 1.0)
        scalar_product = vec1.scalar_product(vec2.x, vec2.y, vec2.z)
        self.assertEqual(scalar_product, 10.0)

    def test_calc_negative_scalar_product(self):
        vec1 = Vector3d(-4.3, 2.5, -3.0)
        vec2 = Vector3d(3.6, 2.0, -6.6)
        scalar_product = vec1.scalar_product(vec2.x, vec2.y, vec2.z)
        self.assertAlmostEqual(scalar_product, 9.32, 2)

    def test_calc_zero_scalar_product(self):
        vec1 = Vector3d(0.0, 0.0, 0.0)
        vec2 = Vector3d(0.0, 0.0, 0.0)
        scalar_product = vec1.scalar_product(vec2.x, vec2.y, vec2.z)
        self.assertEqual(scalar_product, 0.0)

    def test_calc_simple_vector_product(self):
        vec1 = Vector3d(1.0, 2.0, 3.0)
        vec2 = Vector3d(3.0, 2.0, 1.0)
        vector_product = vec1.vector_product(vec2.x, vec2.y, vec2.z)
        vec_params = [-4.0, -8.0, -4.0]
        for val1, val2 in zip(vector_product, vec_params):
            self.assertAlmostEqual(val1, val2, 0)

    def test_calc_negative_vector_product(self):
        vec1 = Vector3d(-4.3, 2.5, -3.0)
        vec2 = Vector3d(3.6, 2.0, -6.6)
        vector_product = vec1.vector_product(vec2.x, vec2.y, vec2.z)
        vec_params = [-10.5, 39.18, -17.6]
        for val1, val2 in zip(vector_product, vec_params):
            self.assertAlmostEqual(val1, val2, 2)

    def test_calc_zero_vector_product(self):
        vec1 = Vector3d(0.0, 0.0, 0.0)
        vec2 = Vector3d(0.0, 0.0, 0.0)
        vector_product = vec1.vector_product(vec2.x, vec2.y, vec2.z)
        vec_params = [0.0, 0.0, 0.0]
        for val1, val2 in zip(vector_product, vec_params):
            self.assertAlmostEqual(val1, val2, 0)
