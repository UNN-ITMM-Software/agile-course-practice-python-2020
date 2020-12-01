import unittest

from gerasimov_dmitry_lab1.viewmodel.quadratic_equation_viewmodel import QuadraticEquationViewModel


class MyTestCase(unittest.TestCase):
    def test_by_default_button_is_disable(self):
        model = QuadraticEquationViewModel()
        self.assertEqual('disabled', model.is_button_enable())

    def test_when_enter_a_b_c_button_enabled(self):
        model = QuadraticEquationViewModel(1, 1, 1)
        self.assertTrue(model.is_button_enable())

    def test_when_clear_a_button_disabled(self):
        model = QuadraticEquationViewModel(1, -1, 1)
        model.set_a(None)
        self.assertEqual('disabled', model.is_button_enable())

    def test_when_clear_b_button_disabled(self):
        model = QuadraticEquationViewModel(1, -1, 1)
        model.set_b(None)
        self.assertEqual('disabled', model.is_button_enable())

    def test_when_clear_c_button_disabled(self):
        model = QuadraticEquationViewModel(1, -1, 1)
        model.set_c(None)
        self.assertEqual('disabled', model.is_button_enable())

    def test_when_enter_values_display_result(self):
        model = QuadraticEquationViewModel(2, 4, 2)
        model.perform()
        answer = 'Answer:\n x = -1.0'
        self.assertEqual(answer, model.get_result())

    def test_when_enter_incorrect_values(self):
        model = QuadraticEquationViewModel('-1a', '123', 'q9')
        self.assertEqual('disabled', model.is_button_enable())

    def test_correct_set_value(self):
        model = QuadraticEquationViewModel()
        model.set_a(1)
        model.set_b(10)
        model.set_c(-12)

        self.assertEqual(1, model.get_a())
        self.assertEqual(10, model.get_b())
        self.assertEqual(-12, model.get_c())
