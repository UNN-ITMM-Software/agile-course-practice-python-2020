import unittest

from modified_stack.model.modified_stack import ModifiedStack


class TestModifiedStack(unittest.TestCase):
    def test_can_create_empty__stack(self):
        stack = ModifiedStack()
        self.assertTrue(isinstance(stack, ModifiedStack))

    def test_can_create_stack_from_list(self):
        stack = ModifiedStack([1, 2, 6, 7, 8])
        self.assertEqual(stack.look_top(), 8)

    def test_raise_when_create_stack_with_not_list(self):
        with self.assertRaises(TypeError):
            ModifiedStack({'key1': 1, 'key2': 2})

    def test_raise_when_create_dheap_with_float_d(self):
        with self.assertRaises(TypeError):
            ModifiedStack([1, 2.0, 3, set()])

    def test_is_empty(self):
        stack = ModifiedStack()
        self.assertTrue(stack.is_empty())

    def test_in_not_empty(self):
        stack = ModifiedStack([1, 2, 3, 4])
        self.assertFalse(stack.is_empty())

    def test_size_return_zero_for_empty_stack(self):
        stack = ModifiedStack()
        self.assertEqual(stack.size(), 0)

    def test_size_not_zero(self):
        stack = ModifiedStack([1, 2, 3, 4])
        self.assertEqual(stack.size(), 4)

    def test_can_look_top(self):
        stack = ModifiedStack([34, 467, 567, 768])
        self.assertEqual(stack.look_top(), 768)

    def test_look_top_return_none_if_stack_empty(self):
        stack = ModifiedStack()
        self.assertEqual(stack.look_top(), None)

    def test_push_in_empty_stack(self):
        stack = ModifiedStack()
        stack.push(2)
        self.assertEqual(stack.look_top(), 2)

    def test_can_push_one_elem_in_stack(self):
        stack = ModifiedStack([2])
        stack.push(3)
        self.assertEqual(stack.look_top(), 3)

    def test_push_one_change_min(self):
        stack = ModifiedStack([2])
        stack.push(-5)
        self.assertEqual(stack.find_min(), -5)

    def test_can_pop_one_from_stack(self):
        stack = ModifiedStack()
        stack.push([20, 7, 56, 23])
        stack.pop()
        self.assertEqual(stack.look_top(), 56)

    def test_can_pop_more_then_one_from_stack(self):
        stack = ModifiedStack()
        stack.push([20, 7, 56, 23])
        stack.pop(3)
        self.assertEqual(stack.look_top(), 20)

    def test_raise_pop_if_count_more_then_stack_size(self):
        stack = ModifiedStack()
        stack.push([20, 7, 56, 23])
        with self.assertRaises(ValueError):
            stack.pop(200)

    def test_raise_when_count_in_pop_not_positive(self):
        with self.assertRaises(ValueError):
            stack = ModifiedStack([1, 45, 67, 67])
            stack.pop(-3)

    def test_raise_when_count_in_pop_not_int(self):
        with self.assertRaises(ValueError):
            stack = ModifiedStack([1, 45, 67, 67])
            stack.pop(-3.5)

    def test_can_find_min_in_stack(self):
        stack = ModifiedStack()
        stack.push([10, 20])
        self.assertEqual(stack.find_min(), 10)

    def test_find_min_return_none_if_stack_empty(self):
        stack = ModifiedStack()
        self.assertEqual(stack.find_min(), None)
