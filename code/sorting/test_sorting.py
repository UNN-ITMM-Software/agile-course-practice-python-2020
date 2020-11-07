import unittest

from sorting.sorting import Sorting


# [0,7,4] -> [0,4,7]

class SortingTest(unittest.TestCase):
    def test_can_create_sorting(self):
        sorting = Sorting([])
        self.assertTrue(isinstance(sorting, Sorting))

    def test_init_param_list(self):
        arr = [1, 2, 3]
        self.assertEqual(arr, Sorting(arr).array)

    def test_can_sort_0_7_4(self):
        sort = Sorting([0, 7, 4])
        self.assertEqual(sort.sorting_func(), [0, 4, 7])


if __name__ == '__main__':
    unittest.main()
