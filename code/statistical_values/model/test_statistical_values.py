import unittest

from statistical_values.model.statistical_values import StatisticalValues


class TestStatisticalValuesClass(unittest.TestCase):
    def test_can_create_from_array(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3])
        # Act & Assert
        self.assertTrue(isinstance(stat, StatisticalValues))

    def test_can_create_from_tuple(self):
        # Arrange
        stat = StatisticalValues((1, 2, 3))
        # Act & Assert
        self.assertTrue(isinstance(stat, StatisticalValues))

    def test_can_create_from_int(self):
        # Arrange
        stat = StatisticalValues(1)
        # Act & Assert
        self.assertTrue(isinstance(stat, StatisticalValues))

    def test_can_create_from_float(self):
        # Arrange
        stat = StatisticalValues(1.0)
        # Act & Assert
        self.assertTrue(isinstance(stat, StatisticalValues))

    def test_raises_on_incorrect_type(self):
        with self.assertRaises(TypeError):
            StatisticalValues('d')

    def test_raises_on_empty(self):
        with self.assertRaises(TypeError):
            StatisticalValues()


class TestStatisticalValuesOperations(unittest.TestCase):
    def test_can_compute_mean(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3, 2])
        # Act
        mean = stat.mean()
        # Assert
        self.assertEqual(mean, 2.0)

    def test_can_compute_mean_one_element(self):
        # Arrange
        stat = StatisticalValues(1)
        # Act
        mean = stat.mean()
        # Assert
        self.assertEqual(mean, 1.0)

    def test_can_compute_var(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3, 2])
        # Act
        var = stat.variance()
        # Assert
        self.assertEqual(var, 0.5)

    def test_can_compute_var_one_element(self):
        # Arrange
        stat = StatisticalValues(1)
        # Act
        var = stat.variance()
        # Assert
        self.assertEqual(var, 0)

    def test_can_compute_median(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3, 2])
        # Act
        median = stat.median()
        # Assert
        self.assertEqual(median, 2.0)

    def test_can_compute_even_median(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3, 3, 5])
        # Act
        median = stat.median()
        # Assert
        self.assertEqual(median, 3.0)

    def test_can_compute_median_one_element(self):
        # Arrange
        stat = StatisticalValues(1)
        # Act
        median = stat.median()
        # Assert
        self.assertEqual(median, 1)

    def test_can_compute_begining_moment(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3, 2])
        # Act
        bmoment = stat.begining_moment(k=1)
        # Assert
        self.assertEqual(bmoment, 2.0)

    def test_can_compute_kth_begining_moment(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3, 2])
        # Act
        bmoment = stat.begining_moment(k=3)
        # Assert
        self.assertEqual(bmoment, 11.0)

    def test_bmoment_raises_on_incorrect_k(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3, 2])
        # Act & Assert
        with self.assertRaises(ValueError):
            stat.begining_moment(k=0)

    def test_bmoment_raises_on_neg_k(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3, 2])
        # Act & Assert
        with self.assertRaises(ValueError):
            stat.begining_moment(k=-1)

    def test_can_compute_central_moment(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3, 2])
        # Act
        cmoment = stat.central_moment(k=2)
        # Assert
        self.assertEqual(cmoment, 0.5)

    def test_cmoment_raises_on_incorrect_k(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3, 2])
        # Act & Assert
        with self.assertRaises(ValueError):
            stat.central_moment(k=0)

    def test_cmoment_raises_on_neg_k(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3, 2])
        # Act & Assert
        with self.assertRaises(ValueError):
            stat.central_moment(k=-1)

    def test_can_compute_kth_central_moment(self):
        # Arrange
        stat = StatisticalValues([1, 2, 3, 2])
        # Act
        cmoment = stat.central_moment(k=4)
        # Assert
        self.assertEqual(cmoment, 0.5)
