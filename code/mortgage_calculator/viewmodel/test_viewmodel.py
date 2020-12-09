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
