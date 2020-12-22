import unittest
from galochkin_aleksei_lab_1.viewmodel.viewmodel import NodeViewModel


class MyTestCase(unittest.TestCase):
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

    # def test_clear_output_error(self):
    #     view_model = NodeViewModel()
    #     view_model.set_input_value("-13,5")
    #     view_model.set_cast_type("kelvin")
    #     view_model.convert()
    #     self.assertAlmostEqual(view_model.get_output_value(), 259.65)
    #
    # def test_converting_case_newton(self):
    #     view_model = NodeViewModel()
    #     view_model.set_input_value("-13,5")
    #     view_model.set_cast_type("newton")
    #     view_model.convert()
    #     self.assertAlmostEqual(view_model.get_output_value(), -4.455)
    #
    # def test_error_converting_case_nan(self):
    #     view_model = NodeViewModel()
    #     view_model.set_input_value("some not a number string")
    #     view_model.convert()
    #     self.assertEqual(view_model.get_error(), "The value is not numeric.\nEnter a numeric value.")
    #
    # def test_output_converting_case_nan(self):
    #     view_model = NodeViewModel()
    #     view_model.set_input_value("some not a number string")
    #     view_model.convert()
    #     self.assertEqual(view_model.get_output_value(), '')
    #
    # def test_clear_output(self):
    #     view_model = NodeViewModel()
    #     view_model.set_input_value("-13,5")
    #     view_model.set_cast_type("newton")
    #     view_model.convert()
    #     view_model.clear_output()
    #     self.assertEqual(view_model.get_output_value(), '')
    #
    # def test_clear_error(self):
    #     view_model = NodeViewModel()
    #     view_model.set_input_value("some not a number string")
    #     view_model.convert()
    #     view_model.clear_error()
    #     self.assertEqual(view_model.get_error(), '')
