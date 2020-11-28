import unittest

from prime_numbers.model.prime_numbers import Range, get_primers
from prime_numbers.model.prime_numbers import RangeError


class PrimeNumbersTests(unittest.TestCase):
    def check_positive_valid_range(self):
        test_range = Range(start=0, end=25)
        self.assertTrue(isinstance(test_range, Range))

    def check_negative_valid_range(self):
        test_range = Range(-10, -5)
        self.assertTrue(isinstance(test_range, Range))

    def check_positive_invalid_range(self):
        with self.assertRaises(RangeError):
            Range(start=100, end=25)

    def check_negative_invalid_range(self):
        with self.assertRaises(RangeError):
            Range(-5, -25)

    def test_can_write_range_as_string(self):
        test_range = Range(0, 5)
        self.assertEqual(str(test_range), 'range(0, 5)')
        self.assertEqual('range(0, 5)', test_range.__str__())

    def test_can_return_prime_numbers_in_range_0_10(self):
        test_range = Range(0, 10)
        prime_numbers = get_primers(test_range)
        ref = [2, 3, 5, 7]
        self.assertEqual(prime_numbers, ref)

    def test_can_return_prime_numbers_in_range_0_0(self):
        test_range = Range(0, 0)
        prime_numbers = get_primers(test_range)
        ref = []
        self.assertEqual(prime_numbers, ref)

    def test_can_return_prime_numbers_in_neg_pos_range_10_10(self):
        test_range = Range(-10, 15)
        prime_numbers = get_primers(test_range)
        ref = [2, 3, 5, 7, 11, 13]
        self.assertEqual(prime_numbers, ref)

    def test_can_return_prime_numbers_in_neg_range_10_0(self):
        test_range = Range(-10, 0)
        prime_numbers = get_primers(test_range)
        ref = []
        self.assertEqual(prime_numbers, ref)
