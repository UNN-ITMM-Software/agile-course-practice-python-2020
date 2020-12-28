import unittest
from tree_viewmodel.viewmodel.tree_viewmodel import TreeViewModel


class TestViewModel(unittest.TestCase):
    def test_default_enable_input_button(self):
        model = TreeViewModel()
        self.assertEqual('disabled', model.is_input_button_enable())

    def test_default_enable_find_button(self):
        model = TreeViewModel()
        self.assertEqual('disabled', model.is_find_button_enable())

    def test_validate_with_valide_input_value(self):
        model = TreeViewModel()
        model.set_input_value(5)
        self.assertEqual('normal', model.is_input_button_enable())

    def test_validate_with_invalide_input_value(self):
        model = TreeViewModel()
        model.set_input_value('f')
        self.assertEqual('disabled', model.is_input_button_enable())

    def test_validate_with_valide_find_value(self):
        model = TreeViewModel()
        model.set_find_value(8)
        self.assertEqual('normal', model.is_find_button_enable())

    def test_validate_with_invalide_find_value(self):
        model = TreeViewModel()
        model.set_find_value('f')
        self.assertEqual('disabled', model.is_find_button_enable())

    def test_input_output_result(self):
        model = TreeViewModel()
        model.set_input_value(10)
        model.input_click()
        model.set_find_value(10)
        model.find_click()
        self.assertEqual(model.get_find_result(), 10)

    def test_get_tree(self):
        model = TreeViewModel()
        model.set_input_value(1)
        model.input_click()
        model.set_input_value(2)
        model.input_click()
        self.assertEqual(model.get_tree_values(), [1, 2])
