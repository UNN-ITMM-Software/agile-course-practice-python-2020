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

    def test_can_convert_str_to_int(self):
        sort = Sorting([0, 1, '2', '45', 4, '8'])
        self.assertEqual(sort.convert_to_array_of_int(), [0, 1, 2, 45, 4, 8])

    def test_can_resolv_words(self):
        sort = Sorting([1, '45', 3, 'erf', '5'])
        self.assertEqual(sort.convert_to_array_of_int(), [1, 45, 3, 5])

