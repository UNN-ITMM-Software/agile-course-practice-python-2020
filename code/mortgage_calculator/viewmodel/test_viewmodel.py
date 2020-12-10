import unittest

from mortgage_calculator.viewmodel.viewmodel import MortgageViewModel


class TestMortgageViewModel(unittest.TestCase):
    def setUp(self):
        self.view_model = MortgageViewModel()

    def test_by_default_button_calculate_monthly_payment_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_calculate_monthly_payment_state())

    def test_by_default_button_calculate_expected_term_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_calculate_expected_term_state())

    def test_by_default_button_calculate_overpaid_amount_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_calculate_overpaid_amount_state())

    def test_when_entered_correct_parameters_all_buttons_enabled(self):
        self.view_model.set_amount('1')
        self.view_model.set_initial_payment('1')
        self.view_model.set_rate('1')
        self.view_model.set_term('1')
        self.view_model.set_monthly_payment('1')

        self.assertNotEqual('disabled', self.view_model.get_button_calculate_monthly_payment_state())
        self.assertNotEqual('disabled', self.view_model.get_button_calculate_expected_term_state())
        self.assertNotEqual('disabled', self.view_model.get_button_calculate_overpaid_amount_state())

    def test_when_entered_incorrect_parameters_all_buttons_disabled(self):
        self.view_model.set_amount('1')
        self.view_model.set_initial_payment('')
        self.view_model.set_rate('1')

        self.assertEqual('disabled', self.view_model.get_button_calculate_monthly_payment_state())
        self.assertEqual('disabled', self.view_model.get_button_calculate_expected_term_state())
        self.assertEqual('disabled', self.view_model.get_button_calculate_overpaid_amount_state())
