import operator
import numpy as np

from mortgage_calculator.model.mortgage import Mortgage
from mortgage_calculator.model.term_types import TermType


class MortgageViewModel:
    term_type_to_str = {TermType.MONTHLY: 'months', TermType.YEARLY: 'years'}
    str_to_term_type = {'months': TermType.MONTHLY, 'years': TermType.YEARLY}

    @staticmethod
    def is_positive_number(number: str) -> bool:
        return number != '' and np.all(list(map(operator.methodcaller("isdigit"), number)))

    def __init__(self):
        self.error_message = {'amount': '',
                              'initial_payment': '',
                              'rate': '',
                              'term': '',
                              'monthly_payment': ''}

        self.amount = ''
        self.initial_payment = ''
        self.rate = ''
        self.term = ''
        self.monthly_payment = ''
        self.term_type = TermType.MONTHLY

        self.button_calculate_monthly_payment_state = 'disabled'
        self.button_calculate_expected_term_state = 'disabled'
        self.button_calculate_overpaid_amount_state = 'disabled'

    def validate_text_number(self, number: str, parameter_name: str) -> bool:
        self.error_message[parameter_name] = ''
        correct_number = MortgageViewModel.is_positive_number(number)
        if not correct_number:
            self.error_message[parameter_name] = 'Incorrect values: {}'.format(number)
        return correct_number

    def check_numbers(self):
        amount_correct = self.validate_text_number(self.amount, 'amount')
        initial_payment_correct = self.validate_text_number(self.initial_payment, 'initial_payment')
        rate_correct = self.validate_text_number(self.rate, 'rate')
        term_correct = self.validate_text_number(self.term, 'term')
        monthly_payment = self.validate_text_number(self.monthly_payment, 'monthly_payment')

        if amount_correct and initial_payment_correct and rate_correct:
            self.set_button_calculate_monthly_payment_state('enabled')
        else:
            self.set_button_calculate_monthly_payment_state('disabled')

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

    def get_amount(self):
        return self.amount

    def set_amount(self, value):
        self.amount = value
        self.check_numbers()

    def get_initial_payment(self):
        return self.initial_payment

    def set_initial_payment(self, value):
        self.initial_payment = value
        self.check_numbers()

    def get_rate(self):
        return self.rate

    def set_rate(self, value):
        self.rate = value
        self.check_numbers()


