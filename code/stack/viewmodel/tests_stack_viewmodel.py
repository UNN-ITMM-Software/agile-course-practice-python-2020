import unittest

from stack.viewmodel.stack_viewmodel import StackViewModel

class MyTestCase(unittest.TestCase):
    def test_default_enable_input_button(self):
        model = StackViewModel()
        self.assertEqual('disabled', model.is_input_button_enable())

    def test_default_enable_output_button(self):
        model = StackViewModel()
        self.assertEqual('disabled', model.is_output_button_enable())

    def test_default_enable_size_button(self):
        model = StackViewModel()
        self.assertEqual('disabled', model.is_size_button_enable())

    def test_validate_with_valide_input_size(self):
        model = StackViewModel()
        model.set_size_value(5)
        self.assertEqual('normal', model.is_size_button_enable())

    def test_validate_with_invalide_input_size(self):
        model = StackViewModel()
        model.set_size_value('f')
        self.assertEqual('disabled', model.is_size_button_enable())

    def test_validate_with_valide_input_value(self):
        model = StackViewModel()
        model.set_input_value(5)
        self.assertEqual('normal', model.is_input_button_enable())

    def test_validate_with_invalide_input_value(self):
        model = StackViewModel()
        model.set_input_value('f')
        self.assertEqual('disabled', model.is_input_button_enable())

    def test_input_value_with_int_input_value(self):
        model = StackViewModel()
        model.set_input_value(5)
        self.assertEqual(model.get_input_value(), 5)

    def test_input_value_with_float_input_value(self):
        model = StackViewModel()
        model.set_input_value(5.0)
        self.assertEqual(model.get_input_value(), 5.0)

    def test_input_output_result(self):
        model = StackViewModel()
        model.set_input_value(10)
        model.input_click()
        model.output_click()
        self.assertEqual(model.get_pop_result(), 10)

    def test_get_stack(self):
        model = StackViewModel()
        model.set_input_value(1)
        model.input_click()
        model.set_input_value(2)
        model.input_click()
        self.assertEqual(model.get_stack_values(), [1, 2])
