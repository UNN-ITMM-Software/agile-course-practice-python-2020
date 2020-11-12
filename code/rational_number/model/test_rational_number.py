import unittest

from rational_number.model.rational_number import RationalNumber


class TestRationalNumberClass(unittest.TestCase):
    def test_can_create_rational_number(self):
        number = RationalNumber(-1, 2)
        self.assertTrue(isinstance(number, RationalNumber))

    def test_can_check_equality_rational_numbers(self):
        number = RationalNumber(-1, 2)
        self.assertEquals(number, RationalNumber(-1, 2))
        self.assertEquals(number, RationalNumber(-1, 2))
