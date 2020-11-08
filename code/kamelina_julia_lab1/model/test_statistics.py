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
