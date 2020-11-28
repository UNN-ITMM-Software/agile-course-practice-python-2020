import unittest

from prime_numbers.viewmodel.prime_numbers_viewmodel import PrimeNumberViewModel


class MyTestCase(unittest.TestCase):
    def test_by_default_button_is_disable(self):
        model = PrimeNumberViewModel()
        self.assertEqual('disabled', model.is_button_enable())

    def test_when_enter_both_number_button_enabled(self):
        model = PrimeNumberViewModel(1, 10)

        self.assertTrue(model.is_button_enable())

    def test_when_clear_first_number_button_disabled(self):
        model = PrimeNumberViewModel(1, 10)
        model.set_start_value(None)

        self.assertEqual('disabled', model.is_button_enable())

    def test_when_clear_second_number_button_disabled(self):
        model = PrimeNumberViewModel(1, 10)
        model.set_end_value(None)

        self.assertEqual('disabled', model.is_button_enable())

    def test_when_enter_values_display_corrected_list(self):
        model = PrimeNumberViewModel(1, 10)
        model.perform()
        answer = [2, 3, 5, 7]

        self.assertEqual(answer, model.get_result())

    def test_when_enter_incorrect_values(self):
        model = PrimeNumberViewModel('asd', '11a')
        self.assertEqual('disabled', model.is_button_enable())

    def test_when_first_value_is_bigger_than_second(self):
        model = PrimeNumberViewModel(10, 1)
        model.perform()
        error_message = 'Что-то пошло не так.\nВозможно первое число оказалось больше второго'
        self.assertEqual(error_message, model.get_error_message())
        self.assertIsNone(model.get_result())


if __name__ == '__main__':
    unittest.main()
