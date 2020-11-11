import unittest

from register import Register


class TestAmountOfMarks(unittest.TestCase):
    def test_correct_amount(self):
        result = Register([2, 3]).amount()
        self.assertEqual(result, 2)

    def test_amount_not_negative(self):
        result = Register([2, 3]).amount()
        self.assertGreaterEqual(result, 0)

    def test_amount_not_string(self):
        result = Register([2, 3]).amount()
        self.assertNotIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()