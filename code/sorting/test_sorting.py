import unittest

from sorting.sorting import Sorting


# [0,7,4] -> [0,4,7]

class SortingTest(unittest.TestCase):
    def test_can_create_sorting(self):
        sorting = Sorting()
        self.assertTrue(isinstance(sorting, Sorting))

    def test_can_sort_0_7_4(self):
        array = [0, 7, 4]
        self.assertEqual(Sorting.sorting_func(array=[0, 7, 4]), [0, 4, 7])


if __name__ == '__main__':
    unittest.main()
