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


class TestCorrectInputValue(unittest.TestCase):
    def test_marks_return_error_message_if_arguments_str(self):
        self.assertRaises(ValueError, Register.is_correct, ['two', 'three', 'four', 'five'])

    def test_marks_return_error_message_if_arguments_negative(self):
        self.assertRaises(ValueError, Register.is_correct, [-2, 3, -4, 5])

    def test_marks_return_error_message_if_arguments_less_1(self):
        self.assertRaises(ValueError, Register.is_correct, [3, 1, 0, 5])

    def test_marks_return_error_message_if_arguments_greater_5(self):
        self.assertRaises(ValueError, Register.is_correct, [4, 3, 7, 5])


if __name__ == '__main__':
    unittest.main()