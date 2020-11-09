import unittest

from sorting.sorting import Sorting

FIRST_CASE = [0, 7, 4]
SECOND_CASE = [0, 45, 1,  8, 2, 4]
THIRD_CASE = [0, 4, '45', '1', 2, 8]
FOURTH_CASE = [1, '45', 3, 5, 'wef']
FIFTH_CASE = [0, 5, -1, 56, -7, -44]
SIXTH_CASE = [0.5, 1.5, 1.6, 0.05, 7.5, 3.4]
SEVENTH_CASE = ['123abc', 5, 0, '45']


class SortingTest(unittest.TestCase):
    def test_can_create_sorting(self):
        sorting = Sorting([])
        self.assertTrue(isinstance(sorting, Sorting))

    def test_init_param_list(self):
        arr = [1, 2, 3]
        self.assertEqual(arr, Sorting(arr).array)

    def test_sorting_should_be_list(self):
        arr = [3]
        self.assertTrue(Sorting(arr))

    def test_can_sort_first_case(self):
        sort = Sorting(FIRST_CASE)
        self.assertEqual(sort.insertion_sort(), [0, 4, 7])

    def test_can_convert_str_to_int(self):
        sort = Sorting([0, 1, '2', '45'])
        self.assertEqual(sort.convert_to_array_of_int(), [0, 1, 2, 45])

    def test_can_resolv_words(self):
        sort = Sorting([1, '45', 3, 'erf', '5'])
        self.assertEqual(sort.convert_to_array_of_int(), [1, 45, 3, 5])

    def test_can_sort_second_case(self):
        sort = Sorting(SECOND_CASE)
        self.assertEqual(sort.insertion_sort(), [0, 1, 2, 4, 8, 45])

    def test_can_sort_third_case(self):
        sort = Sorting(THIRD_CASE)
        self.assertEqual(sort.insertion_sort(), [0, 1, 2, 4, 8, 45])

    def test_can_sort_fourth_case(self):
        sort = Sorting(FOURTH_CASE)
        self.assertEqual(sort.insertion_sort(), [1, 3, 5, 45])

    def test_can_sort_negtive_values(self):
        sort = Sorting(FIFTH_CASE)
        self.assertEqual(sort.insertion_sort(), [-44, -7, -1, 0, 5, 56])

    def test_can_sort_float_values(self):
        sort = Sorting(SIXTH_CASE)
        self.assertEqual(sort.insertion_sort(), [0.05, 0.5, 1.5, 1.6, 3.4, 7.5])

    def test_can_sort_seventh_case(self):
        sort = Sorting(SEVENTH_CASE)
        self.assertEqual(sort.insertion_sort(), [0, 5, 45])
