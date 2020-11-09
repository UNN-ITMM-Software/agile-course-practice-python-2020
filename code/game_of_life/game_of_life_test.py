import unittest

from game_of_life import StrCalculator


class TestStrCalculatorClass(unittest.TestCase):

    def test_add_empty_string_is_7(self):
        strcalc = StrCalculator()
        result = strcalc.add("")
        self.assertTrue(result == 7)
