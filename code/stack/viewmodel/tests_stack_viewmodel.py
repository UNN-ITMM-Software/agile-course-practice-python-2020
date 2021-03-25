import unittest

from stack.viewmodel.stack_viewmodel import StackViewModel


class TestStackViewModel(unittest.TestCase):
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


class TestViewModelLogger(unittest.TestCase):
    def test_init_stack_logging(self):
        model = StackViewModel()
        self.assertEqual('Program started', model.logger.get_last_message())

    def test_validate_with_valide_input_size_logging(self):
        model = StackViewModel()
        model.set_size_value(5)
        model.size_click()
        self.assertEqual('Размер стека изменен на  5', model.logger.get_last_message())

    def test_validate_with_invalide_input_size_logging(self):
        model = StackViewModel()
        model.set_size_value('р')
        model.size_click()
        self.assertEqual('Неверный тип для размера стека', model.logger.get_last_message())

    def test_validate_with_valide_input_value_logging(self):
        model = StackViewModel()
        model.set_input_value(6)
        model.input_click()
        self.assertEqual('Число 6 добавлено в стек', model.logger.get_last_message())

    def test_validate_with_invalide_input_value_logging(self):
        model = StackViewModel()
        model.set_input_value('f')
        model.input_click()
        self.assertEqual('Введение данных неверного типа', model.logger.get_last_message())

    def test_output_result_logging(self):
        model = StackViewModel()
        model.set_input_value(3)
        model.input_click()
        model.set_input_value(10)
        model.input_click()
        model.output_click()
        self.assertEqual('Получено число 10', model.logger.get_last_message())

    def test_empty_stack_output_result_logging(self):
        model = StackViewModel()
        model.set_input_value(10)
        model.input_click()
        model.output_click()
        self.assertEqual('Стэк пуст', model.logger.get_last_message())

    def test_full_stack_logging(self):
        model = StackViewModel()
        model.set_size_value(2)
        model.size_click()
        model.set_input_value(10)
        model.input_click()
        model.set_input_value(6)
        model.input_click()
        self.assertEqual('Стэк переполнен', model.logger.get_last_message())
