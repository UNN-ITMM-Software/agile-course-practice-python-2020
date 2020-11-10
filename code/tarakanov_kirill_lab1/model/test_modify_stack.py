import unittest

from tarakanov_kirill_lab1.model.modify_stack import ModifyStack


class TestModifyStack(unittest.TestCase):
    def test_can_create_empty_modify_stack(self):
        stack = ModifyStack()
        self.assertTrue(isinstance(stack, ModifyStack))

    def test_is_empty(self):
        stack = ModifyStack()
        self.assertTrue(stack.is_empty(), True)

    def test_size_return_zero_for_empty_stack(self):
        stack = ModifyStack()
        self.assertEqual(stack.size(), 0)

    def test_push_in_empty_stack_and_look_top_then(self):
        stack = ModifyStack()
        stack.push(2)
        self.assertEqual(stack.look_top(), 2)
