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

        self.click_calculate_monthly_payment_result = ''
        self.click_calculate_expected_term_result = ''
        self.click_calculate_overpaid_amount_result = ''

    def validate_text_number(self, number: str, parameter_name: str) -> bool:
        self.error_message[parameter_name] = ''
        correct_number = MortgageViewModel.is_positive_number(number)
        if not correct_number and number != '':
            self.error_message[parameter_name] = 'Incorrect values: {}'.format(number)
        return correct_number

    def check_numbers(self):
        amount_correct = self.validate_text_number(self.amount, 'amount')
        initial_payment_correct = self.validate_text_number(self.initial_payment, 'initial_payment')
        rate_correct = self.validate_text_number(self.rate, 'rate')
        term_correct = self.validate_text_number(self.term, 'term')
        monthly_payment_correct = self.validate_text_number(self.monthly_payment, 'monthly_payment')

        if amount_correct and initial_payment_correct and rate_correct and\
                term_correct and monthly_payment_correct:
            self.set_button_calculate_monthly_payment_state('enabled')
            self.set_button_calculate_expected_term_state('enabled')
            self.set_button_calculate_overpaid_amount_state('enabled')
        else:
            self.set_button_calculate_monthly_payment_state('disabled')
            self.set_button_calculate_expected_term_state('disabled')
            self.set_button_calculate_overpaid_amount_state('disabled')

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

    def get_term(self):
        return self.term

    def set_term(self, value):
        self.term = value
        self.check_numbers()

    def get_monthly_payment(self):
        return self.monthly_payment

    def set_monthly_payment(self, value):
        self.monthly_payment = value
        self.check_numbers()

    def get_term_type(self):
        return self.term_type_to_str[self.term_type]

    def set_term_type(self, value):
        self.term_type = self.str_to_term_type[value]

    def get_click_calculate_monthly_payment_result(self):
        return self.click_calculate_monthly_payment_result

    def get_click_calculate_expected_term_result(self):
        return self.click_calculate_expected_term_result

    def get_click_calculate_overpaid_amount_result(self):
        return self.click_calculate_overpaid_amount_result

    def get_error_message(self):
        beauty_message = ''
        for key, value in self.error_message.items():
            beauty_message += '\t{}: {}\n'.format(key, value)
        return 'Errors: \n{}'.format(beauty_message)

    def click_calculate_monthly_payment(self):
        if self.button_calculate_monthly_payment_state != 'disabled':
            mc = self.__get_mortgage_calculator()
            result = mc.calculate_monthly_payment()
            self.click_calculate_monthly_payment_result = str(result)

    def click_calculate_expected_term(self):
        if self.button_calculate_expected_term_state != 'disabled':
            mc = self.__get_mortgage_calculator()
            result = mc.calculate_expected_term()
            self.click_calculate_expected_term_result = str(result)

    def click_calculate_overpaid_amount(self):
        if self.button_calculate_overpaid_amount_state != 'disabled':
            mc = self.__get_mortgage_calculator()
            result = mc.calculate_overpaid_amount()
            self.click_calculate_overpaid_amount_result = str(result)

    def __get_mortgage_calculator(self):
        return Mortgage(amount=float(self.amount),
                        initial_payment=float(self.initial_payment),
                        rate=float(self.rate),
                        term=float(self.term),
                        term_type=self.term_type,
                        monthly_payment=float(self.monthly_payment))
