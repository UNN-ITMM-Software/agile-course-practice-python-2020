import unittest

from modified_stack.viewmodel.modified_stack_viewmodel import ModifiedStackViewModel


class TestModifiedStackViewModel(unittest.TestCase):

    def test_default_stack_is_empty(self):
        model = ModifiedStackViewModel()

        self.assertEqual(0, model.size())

    def test_pop_from_empty_stack(self):
        model = ModifiedStackViewModel()

        model.set_pop_size(1)
        model.pop()

        self.assertEqual('count should be positive', model.get_error_message())

    def test_get_min_from_empty_stack(self):
        model = ModifiedStackViewModel()

        model.get_min()

        self.assertEqual('Stack is empty', model.get_error_message())

    def test_look_top_from_empty_stack(self):
        model = ModifiedStackViewModel()

        model.get_top()

        self.assertEqual('Stack is empty', model.get_error_message())

    def test_correct_min_value(self):
        model = ModifiedStackViewModel()

        model.set_push_state('N')
        model.set_input_array([5, 1, 6, 7])
        model.push()
        model.get_min()

        self.assertEqual(1, model.min)

    def test_correct_top_value(self):
        model = ModifiedStackViewModel()

        model.set_push_state('One')
        model.set_pushed_element(6)
        model.push()
        model.get_top()

        self.assertEqual(6, model.top)

    def test_when_pushed_value_non_int(self):
        model = ModifiedStackViewModel()

        model.set_push_state('One')
        model.set_pushed_element('PUSH ME')
        model.push()

        self.assertEqual('Input contains non int value', model.get_error_message())

    def test_when_pop_size_non_int(self):
        model = ModifiedStackViewModel()

        model.set_pop_size('AND THEN JUST POP ME')
        model.pop()

        self.assertEqual('Input contains non int value', model.get_error_message())
