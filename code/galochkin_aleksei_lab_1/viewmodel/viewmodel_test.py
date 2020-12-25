import unittest
from galochkin_aleksei_lab_1.viewmodel.viewmodel import NodeViewModel


class ViewModelTest(unittest.TestCase):
    def test_create_view_model(self):
        view_model = NodeViewModel()
        self.assertTrue(isinstance(view_model, NodeViewModel))

    def test_input_value_setter(self):
        view_model = NodeViewModel()
        view_model.set_input_value(15)
        self.assertEqual(view_model.get_input_value(), 15)

    def test_add_node(self):
        view_model = NodeViewModel()
        view_model.set_input_value(1)
        view_model.add_node()
        self.assertEqual(view_model.get_output_value(), [1])

    def test_add_one_more_node(self):
        view_model = NodeViewModel()
        view_model.set_input_value(1)
        view_model.add_node()
        view_model.set_input_value(2)
        view_model.add_node()
        self.assertEqual(view_model.get_output_value(), [2, 1])

    def test_remove_node(self):
        view_model = NodeViewModel()
        view_model.set_input_value(1)
        view_model.add_node()
        view_model.set_input_value(2)
        view_model.add_node()
        view_model.remove_node()
        self.assertEqual(view_model.get_output_value(), [1])

    def test_add_with_error(self):
        view_model = NodeViewModel()
        view_model.set_input_value("String")
        view_model.add_node()
        self.assertEqual(view_model.get_error(), "Please enter numeric positive value")
