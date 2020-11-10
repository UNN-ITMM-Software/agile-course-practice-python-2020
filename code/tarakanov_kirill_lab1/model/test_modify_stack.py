import unittest

from tarakanov_kirill_lab1.model.modify_stack import ModifyStack


class TestModifyStack(unittest.TestCase):
    def test_can_create_empty__stack(self):
        stack = ModifyStack()
        self.assertTrue(isinstance(stack, ModifyStack))

    def test_can_create_stack_from_list(self):
        stack = ModifyStack([1, 2, 6, 7, 8])
        self.assertEqual(stack.look_top(), 8)

    def test_raise_when_create_stack_with_not_list(self):
        with self.assertRaises(TypeError):
            ModifyStack({'key1': 1, 'key2': 2})

    def test_raise_when_create_dheap_with_float_d(self):
        with self.assertRaises(TypeError):
            ModifyStack([1, 2.0, 3, set()])

    def test_is_empty(self):
        stack = ModifyStack()
        self.assertTrue(stack.is_empty())

    def test_in_not_empty(self):
        stack = ModifyStack([1, 2, 3, 4])
        self.assertFalse(stack.is_empty())

    def test_size_return_zero_for_empty_stack(self):
        stack = ModifyStack()
        self.assertEqual(stack.size(), 0)

    def test_size_not_zero(self):
        stack = ModifyStack([1, 2, 3, 4])
        self.assertEqual(stack.size(), 4)

    def test_push_in_empty_stack_and_look_top_then(self):
        stack = ModifyStack()
        stack.push(2)
        self.assertEqual(stack.look_top(), 2)

    def test_can_push_one_elem_in_stack(self):
        stack = ModifyStack()
        stack.push(2)
        stack.push(-5)
        self.assertEqual(stack.look_top(), -5)

    def can_push_more_then_one_elem(self):
        stack = ModifyStack()
        stack.push([1, 2, 3, 4, 5])
        self.assertEqual(stack.look_top(), 5)

    def test_can_pop_one_from_stack(self):
        stack = ModifyStack()
        stack.push([20, 7, 56, 23])
        stack.pop()
        self.assertEqual(stack.look_top(), 56)

    def test_can_pop_more_then_one_from_stack(self):
        stack = ModifyStack()
        stack.push([20, 7, 56, 23])
        stack.pop(3)
        self.assertEqual(stack.look_top(), 20)

    def test_can_find_min_in_stack(self):
        stack = ModifyStack()
        stack.push([10, 20])
        self.assertEqual(stack.find_min(), 10)
