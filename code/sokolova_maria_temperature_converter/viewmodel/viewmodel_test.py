import unittest
from sokolova_maria_temperature_converter.viewmodel.viewmodel import TemperatureConverterViewModel


class MyTestCase(unittest.TestCase):
    def test_create_view_model(self):
        view_model = TemperatureConverterViewModel()
        self.assertTrue(isinstance(view_model, TemperatureConverterViewModel))

    def test_preset_cast_type(self):
        view_model = TemperatureConverterViewModel()
        self.assertEqual(view_model.cast_type, 'fahrenheit')

    def test_input_value_setter(self):
        view_model = TemperatureConverterViewModel()
        view_model.set_input_value(15.8)
        self.assertEqual(view_model.get_input_value(), 15.8)

    def test_cast_type_setter(self):
        view_model = TemperatureConverterViewModel()
        view_model.set_cast_type('newton')
        self.assertEqual(view_model.get_cast_type(), 'newton')

    def test_converting_case_fahrenheit(self):
        view_model = TemperatureConverterViewModel()
        view_model.set_input_value("-13,5")
        view_model.convert()
        self.assertAlmostEqual(view_model.get_output_value(), 7.7)

    def test_converting_case_kelvin(self):
        view_model = TemperatureConverterViewModel()
        view_model.set_input_value("-13,5")
        view_model.set_cast_type("kelvin")
        view_model.convert()
        self.assertAlmostEqual(view_model.get_output_value(), 259.65)

    def test_converting_case_newton(self):
        view_model = TemperatureConverterViewModel()
        view_model.set_input_value("-13,5")
        view_model.set_cast_type("newton")
        view_model.convert()
        self.assertAlmostEqual(view_model.get_output_value(), -4.455)

    def test_error_converting_case_nan(self):
        view_model = TemperatureConverterViewModel()
        view_model.set_input_value("some not a number string")
        view_model.convert()
        self.assertEqual(view_model.get_error(), "The value is not numeric.\nEnter a numeric value.")

    def test_output_converting_case_nan(self):
        view_model = TemperatureConverterViewModel()
        view_model.set_input_value("some not a number string")
        view_model.convert()
        self.assertEqual(view_model.get_output_value(), '')

    def test_clear_output(self):
        view_model = TemperatureConverterViewModel()
        view_model.set_input_value("-13,5")
        view_model.set_cast_type("newton")
        view_model.convert()
        view_model.clear_output()
        self.assertEqual(view_model.get_output_value(), '')

    def test_clear_error(self):
        view_model = TemperatureConverterViewModel()
        view_model.set_input_value("some not a number string")
        view_model.convert()
        view_model.clear_error()
        self.assertEqual(view_model.get_error(), '')
