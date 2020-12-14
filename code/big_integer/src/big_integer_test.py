import unittest

from big_integer import BigInteger


class TestBigIntegerClass(unittest.TestCase):

    def test_big_integer_can_create(self):
        big_integer = BigInteger()
        self.assertTrue(isinstance(big_integer, BigInteger))

    def test_big_integer_can_create_empty(self):
        big_integer = BigInteger([])
        self.assertTrue(isinstance(big_integer, BigInteger))

    def test_big_integer_can_create_full(self):
        big_integer = BigInteger([2, 1, 4])
        self.assertTrue(isinstance(big_integer, BigInteger))

    def test_big_integer_eq_true(self):
        a = BigInteger([1, 1, 1])
        b = BigInteger([1, 1, 1])
        self.assertEqual(a, b)

    def test_big_integer_eq_false(self):
        a = BigInteger([1, 1, 1])
        b = BigInteger([2, 1, 1])
        self.assertNotEqual(a, b)

    def test_big_integer_eq_false_diff_size(self):
        a = BigInteger([1, 1, 1])
        b = BigInteger([2, 1, 1, 4, 5])
        self.assertNotEqual(a, b)

    def test_big_integer_eq_false_empty(self):
        a = BigInteger()
        b = BigInteger([2, 1, 1, 4, 5])
        self.assertNotEqual(a, b)

    def test_big_integer_eq_true_empty(self):
        a = BigInteger()
        b = BigInteger()
        self.assertEqual(a, b)

    def test_big_integer_eq_true_empty_diff(self):
        a = BigInteger()
        b = BigInteger([])
        self.assertEqual(a, b)

    def test_big_integer_add_empty_to_empty(self):
        a = BigInteger()
        b = BigInteger()
        c = a + b
        self.assertEqual(c, BigInteger())

    def test_big_integer_add_full_to_full(self):
        a = BigInteger([1, 2, 3])
        b = BigInteger([5, 5])
        c = a + b
        self.assertEqual(c, BigInteger([6, 7, 3]))

    def test_big_integer_add_full_to_empty(self):
        a = BigInteger([9, 9, 9])
        b = BigInteger()
        c = a + b
        self.assertEqual(c, BigInteger([9, 9, 9]))

    def test_big_integer_add_full_border(self):
        a = BigInteger([9, 9, 9])
        b = BigInteger([9, 5])
        c = a + b
        self.assertEqual(c, BigInteger([8, 5, 0, 1]))

    def test_big_integer_sub_empty_to_empty(self):
        a = BigInteger()
        b = BigInteger()
        c = a - b
        self.assertEqual(c, BigInteger())

    def test_big_integer_sub_full_to_full(self):
        a = BigInteger([6, 7, 3])
        b = BigInteger([5, 5])
        c = a - b
        self.assertEqual(c, BigInteger([1, 2, 3]))

    def test_big_integer_sub_full_to_empty(self):
        a = BigInteger([9, 9, 9])
        b = BigInteger()
        c = a - b
        self.assertEqual(c, BigInteger([9, 9, 9]))

    def test_big_integer_sub_full_border(self):
        a = BigInteger([8, 5, 0, 1])
        b = BigInteger([9, 5])
        c = a - b
        self.assertEqual(c, BigInteger([9, 9, 9]))

    def test_big_integer_mul_empty_to_empty(self):
        a = BigInteger()
        b = BigInteger()
        c = a * b
        self.assertEqual(c, BigInteger())

    def test_big_integer_mul_full_to_full(self):
        a = BigInteger([8, 7, 1])
        b = BigInteger([5, 5])
        c = a * b
        self.assertEqual(c, BigInteger([0, 9, 7, 9]))

    def test_big_integer_mul_full_to_empty(self):
        a = BigInteger([9, 9, 9])
        b = BigInteger()
        c = a * b
        self.assertEqual(c, BigInteger())
