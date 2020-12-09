from mortgage_calculator.model.mortgage import Mortgage


class MortgageViewModel:
    def __init__(self):
        self.error_message_text = ''

        self.amount = ''
        self.initial_payment = ''
        self.rate = ''
        self.term = ''
        self.monthly_payment = ''
        self.term_type = 'months'

        self.button_calculate_monthly_payment_state = 'disabled'
        self.button_calculate_expected_term_state = 'disabled'
        self.button_calculate_overpaid_amount_state = 'disabled'

    def get_button_calculate_monthly_payment_state(self):
        return self.button_calculate_monthly_payment_state

    def set_button_calculate_monthly_payment_state(self, state):
        self.button_calculate_monthly_payment_state = state

    def get_button_calculate_expected_term_state(self):
        return self.button_calculate_expected_term_state

    def set_button_calculate_expected_term_state(self, state):
        self.button_calculate_expected_term_state = state

    def get_button_calculate_overpaid_amount_state(self):
        return self.button_calculate_overpaid_amount_state

    def set_button_calculate_overpaid_amount_state(self, state):
        self.button_calculate_overpaid_amount_state = state


