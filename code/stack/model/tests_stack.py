from stack.model.stack import Stack
import unittest


class StackTestClass(unittest.TestCase):
    def test_create_stack_without_params(self):
        stack = Stack()
        self.assertIsInstance(stack, Stack)

    def test_create_with_valid_size(self):
        stack = Stack(10)
        self.assertIsInstance(stack, Stack)

    def test_create_with_invalid_size_float(self):
        with self.assertRaises(TypeError):
            Stack(0.5)

    def test_create_with_invalid_size_str(self):
        with self.assertRaises(TypeError):
            Stack("0.5")

    def test_create_with_size_less_zero(self):
        with self.assertRaises(Exception):
            Stack(-10)

    def test_create_with_zero_size(self):
        with self.assertRaises(Exception):
            Stack(0)

    def test_push_item(self):
        stack = Stack(10)
        stack.push(7)
        self.assertEqual(stack.pop(), 7)

    def test_push_in_full_stack(self):
        stack = Stack(1)
        stack.push(0)
        with self.assertRaises(Exception):
            stack.push(5)

    def test_pop_from_empty_stack(self):
        stack = Stack(10)
        with self.assertRaises(Exception):
            stack.pop()

    def test_pop_item(self):
        stack = Stack(10)
        stack.push(10)
        self.assertEqual(10, stack.pop())

    def test_push_more_item(self):
        stack = Stack(10)
        stack.push(7)
        stack.push(8)
        stack.push(9)
        self.assertEqual(stack.pop(), 9)

    def test_push_array(self):
        stack = Stack(10)
        stack.push([7, 8, 9])
        self.assertEqual(stack.pop(), 9)

    def test_push_str(self):
        stack = Stack(10)
        stack.push([7, 8, 9])
        stack.push('string')
        self.assertEqual(stack.pop(), 'g')

    def test_oversize_push(self):
        stack = Stack(2)
        with self.assertRaises(Exception):
            stack.push([7, 8, 9])
