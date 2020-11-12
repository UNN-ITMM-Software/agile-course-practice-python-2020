import unittest

from rational_number.model.rational_number import RationalNumber


class TestRationalNumberClass(unittest.TestCase):
    def test_can_create_rational_number(self):
        number = RationalNumber(-1, 2)
        self.assertTrue(isinstance(number, RationalNumber))
