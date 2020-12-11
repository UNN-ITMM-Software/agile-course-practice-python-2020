import unittest

from radix_sort.radix_sort import RadixSort
from random import randint


class TestRadixSortClass(unittest.TestCase):
    def test_create_sorting_object(self):
        radix = RadixSort([])
        self.assertTrue(isinstance(radix, RadixSort))

    def test_radix_sort_with_empty_array(self):
        arr = []
        sorted = RadixSort(arr).sort()
        self.assertEqual(sorted, [])

    def test_radix_sort_with_small_positive_numbers(self):
        arr = [7, 1, 8, 2, 5]
        sorted = RadixSort(arr).sort()
        self.assertEqual(sorted, [1, 2, 5, 7, 8])

    def test_radix_sort_with_small_array(self):
        arr = [1500, 675, 8, 115, 34]
        sorted = RadixSort(arr).sort()
        self.assertEqual(sorted, [8, 34, 115, 675, 1500])

    def test_radix_sort_with_large_array_and_positive_numbers(self):
        size = 10000
        arr = [randint(0, size) for i in range(size)]
        sorted_arr = RadixSort(arr.copy()).sort()
        self.assertEqual(sorted_arr, sorted(arr))

    def test_radix_sort_with_negative_numbers(self):
        arr = [-1, -801, -7, -25, -5]
        sorted = RadixSort(arr).sort()
        self.assertEqual(sorted, [-801, -25, -7, -5, -1])

    def test_radix_sort_with_large_array_and_negative_numbers(self):
        size = 10000
        arr = [randint(-size, 0) for i in range(size)]
        sorted_arr = RadixSort(arr.copy()).sort()
        self.assertEqual(sorted_arr, sorted(arr))

    def test_radix_sort_with_positive_and_negative_numbers(self):
        size = 10000
        arr = [randint(-size, size) for i in range(size)]
        sorted_arr = RadixSort(arr.copy()).sort()
        self.assertEqual(sorted_arr, sorted(arr))

    def test_radix_sort_throws_when_array_is_not_a_list(self):
        arr = "string"
        with self.assertRaises(TypeError):
            RadixSort(arr)

    def test_radix_sort_throws_with_invalid_list(self):
        arr = [1, 'orange', 2, 3, 4, 'apple']
        with self.assertRaises(ValueError):
            RadixSort(arr)

    def test_radix_sort_with_zeroes(self):
        arr = [0, 0, 0]
        sorted = RadixSort(arr).sort()
        self.assertEqual(sorted, [0, 0, 0])

    def test_radix_sort_with_single_element(self):
        arr = [123456789]
        sorted = RadixSort(arr).sort()
        self.assertEqual(sorted, [123456789])
