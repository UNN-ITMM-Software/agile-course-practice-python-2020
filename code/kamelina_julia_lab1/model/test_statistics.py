import unittest

from kamelina_julia_lab1.model.statistics import Statistics


class TestStatisticsClass(unittest.TestCase):
    def test_can_create_from_array(self):
        stat = Statistics([1, 2, 3])
        self.assertTrue(isinstance(stat, Statistics))

    def test_can_create_from_tuple(self):
        stat = Statistics((1, 2, 3))
        self.assertTrue(isinstance(stat, Statistics))

    def test_can_create_from_int(self):
        stat = Statistics(1)
        self.assertTrue(isinstance(stat, Statistics))

    def test_can_create_from_float(self):
        stat = Statistics(1.0)
        self.assertTrue(isinstance(stat, Statistics))

    def test_raises_on_incorrect_type(self):
        with self.assertRaises(TypeError):
            Statistics('d')

    def test_raises_on_empty(self):
        with self.assertRaises(TypeError):
            Statistics()


class TestStatisticsOperations(unittest.TestCase):
    def test_can_compute_mean(self):
        stat = Statistics([1, 2, 3, 2])
        self.assertEqual(stat.mean(), 2.0)

    def test_can_compute_mean_one_element(self):
        stat = Statistics(1)
        self.assertEqual(stat.mean(), 1.0)

    def test_can_compute_var(self):
        stat = Statistics([1, 2, 3, 2])
        self.assertEqual(stat.var(), 0.5)

    def test_can_compute_var_one_element(self):
        stat = Statistics(1)
        self.assertEqual(stat.var(), 0)

    def test_can_compute_median(self):
        stat = Statistics([1, 2, 3, 2])
        self.assertEqual(stat.med(), 2.0)

    def test_can_compute_even_median(self):
        stat = Statistics([1, 2, 3, 3, 5])
        self.assertEqual(stat.med(), 3.0)

    def test_can_compute_median_one_element(self):
        stat = Statistics(1)
        self.assertEqual(stat.med(), 1)
