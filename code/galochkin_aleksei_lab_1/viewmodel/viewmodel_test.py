import unittest
from galochkin_aleksei_lab_1.viewmodel.viewmodel import NodeViewModel
from galochkin_aleksei_lab_1.logger.fake_logger import FakeLogger


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
        self.assertEqual(view_model.get_log_message(), "Error occurred: Please enter numeric positive value")

    def test_remove_intermediate_node(self):
        view_model = NodeViewModel()
        view_model.set_input_value(1)
        view_model.add_node()
        view_model.set_input_value(2)
        view_model.add_node()
        view_model.set_input_value(3)
        view_model.add_node()
        view_model.set_input_value(2)
        view_model.remove_node()
        self.assertEqual(view_model.get_output_value(), [1, 3])

    def test_remove_last_node(self):
        view_model = NodeViewModel()
        view_model.set_input_value(1)
        view_model.add_node()
        view_model.set_input_value(2)
        view_model.add_node()
        view_model.set_input_value(3)
        view_model.add_node()
        view_model.remove_node()
        self.assertEqual(view_model.get_output_value(), [1, 2])

    def test_add_many_nodes(self):
        view_model = NodeViewModel()
        view_model.set_input_value(1)
        view_model.add_node()
        view_model.set_input_value(2)
        view_model.add_node()
        view_model.set_input_value(3)
        view_model.add_node()
        view_model.set_input_value(4)
        view_model.add_node()
        view_model.set_input_value(5)
        view_model.add_node()
        view_model.set_input_value(6)
        view_model.add_node()
        view_model.set_input_value(7)
        view_model.add_node()
        view_model.set_input_value(8)
        view_model.add_node()
        view_model.set_input_value(9)
        view_model.add_node()
        self.assertEqual(view_model.get_output_value(), [1, 3, 2, 5, 7, 9, 8, 6, 4])

    def test_add_node_with_fake_logger(self):
        view_model = NodeViewModel(logger=FakeLogger())
        view_model.set_input_value(1)
        view_model.add_node()
        self.assertEqual(view_model.get_output_value(), [1])
        self.assertEqual(view_model.logger.get_messages(),
                         ['Trying to add node with number 1', 'Node added successfully'])

    def test_remove_node_with_fake_logger(self):
        view_model = NodeViewModel(logger=FakeLogger())
        view_model.set_input_value(1)
        view_model.add_node()
        view_model.set_input_value(2)
        view_model.add_node()
        view_model.remove_node()
        self.assertEqual(view_model.get_output_value(), [1])
        self.assertEqual(view_model.logger.get_messages(),
                         ['Trying to add node with number 1', 'Node added successfully',
                          'Trying to add node with number 2', 'Node added successfully',
                          'Trying to remove node with number 2', 'Node removed successfully'])
