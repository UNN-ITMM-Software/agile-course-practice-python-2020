import unittest

from rational_math import GCD, LCM


class TestMathFunctions(unittest.TestCase):
    def test_GCD_1_1(self):
        self.assertEqual(GCD(1, 1), 1)

    def test_GCD_2_4(self):
        self.assertEqual(GCD(2, 4), 2)

    def test_GCD_81_35(self):
        self.assertEqual(GCD(81, 35), 1)

    def test_LCM_1_2(self):
        self.assertEqual(LCM(1, 2), 2)
