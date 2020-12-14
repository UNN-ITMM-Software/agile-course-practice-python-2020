from sokolova_maria_temperature_converter.model.temperature_converter import TemperatureConverter


class TemperatureConverterViewModel:
    def __init__(self):
        self.input_value = ''
        self.cast_type = 'fahrenheit'
        self.output_value = ''
        self.error = ''

    def get_input_value(self):
        return self.input_value

    def set_input_value(self, value):
        self.input_value = value

    def set_cast_type(self, value):
        self.cast_type = value

    def get_cast_type(self):
        return self.cast_type

    def get_output_value(self):
        return self.output_value

    def clear_output(self):
        self.output_value = ''

    def get_error(self):
        return self.error

    def clear_error(self):
        self.error = ''

    def convert(self):
        try:
            converter = TemperatureConverter(self.input_value)
            self.clear_error()
            if self.cast_type == 'fahrenheit':
                self.output_value = converter.convert_to_fahrenheit()
            elif self.cast_type == 'kelvin':
                self.output_value = converter.convert_to_kelvin()
            elif self.cast_type == 'newton':
                self.output_value = converter.convert_to_newton()

        except ValueError:
            self.clear_output()
            self.error = 'The value is not numeric.\nEnter a numeric value.'
