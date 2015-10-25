import unittest

import rational_math


class TestMathFunctions(unittest.TestCase):
    def test_gcd_1_1(self):
        self.assertEqual(rational_math.gcd(1, 1), 1)

    def test_gcd_2_4(self):
        self.assertEqual(rational_math.gcd(2, 4), 2)

    def test_gcd_81_35(self):
        self.assertEqual(rational_math.gcd(81, 35), 1)

    def test_lcm_1_2(self):
        self.assertEqual(rational_math.lcm(1, 2), 2)

    def test_euclidean_coefficients(self):
        expected_result = [(2, 147), (3, 21), (7, 0)]
        actual_result = rational_math.euclidean_algorithm(1071, 462)
        for actual, expected in zip(actual_result, expected_result):
            self.assertEqual(actual, expected)
