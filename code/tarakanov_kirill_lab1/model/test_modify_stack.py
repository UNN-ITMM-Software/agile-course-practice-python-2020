import unittest

from tarakanov_kirill_lab1.model.modify_stack import ModifyStack


class TestModifyStack(unittest.TestCase):
    def test_can_create_empty_modify_stack(self):
        stack = ModifyStack()
        self.assertTrue(isinstance(stack, ModifyStack))
