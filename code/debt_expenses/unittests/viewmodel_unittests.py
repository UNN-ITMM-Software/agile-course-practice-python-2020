import unittest

from debt_expenses.viewmodel.debt_viewmodel import DebtViewModel


class TestDebtExpensesViewModel(unittest.TestCase):
    def test_by_default_error_is_true(self):
        test_example = DebtViewModel()
        self.assertEqual('Please enter data', test_example.get_error_message())

    def test_when_enter_data(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=4)
        self.assertTrue('Normal work', test_example.get_error_message())

    def test_when_req_sum_incorrect(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=4)
        test_example.set_req_sum(-10)
        self.assertTrue('Error: Incorrect input', test_example.get_error_message())

    def test_when_percent_rate_incorrect(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=4)
        test_example.set_percent_rate(0)
        self.assertTrue('Error: Incorrect input', test_example.get_error_message())

    def test_when_year_incorrect(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=4)
        test_example.set_year(7)
        self.assertTrue('Error: Incorrect input', test_example.get_error_message())

    def test_when_period_incorrect(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=4)
        test_example.set_period(-5)
        self.assertTrue('Error: Incorrect input', test_example.get_error_message())

    def test_when_all_incorrect(self):
        test_example = DebtViewModel(req_sum='@@', percent_rate=-55, period=44, year=-000)
        self.assertTrue('Error: Incorrect input', test_example.get_error_message())


class TestEqualAmountsRepaymentViewModel(unittest.TestCase):
    def test_equal_amounts_repayment_for_1_year(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=1)
        test_example.perform_repayment('equal_amounts')

        payment = test_example.get_payment()
        expenses = test_example.get_expenses()

        answer = 'Payment: 78000 - Expenses: 50000'
        self.assertEqual(answer, 'Payment: {:.0f} - Expenses: {:.0f}'.format(payment, expenses))

    def test_equal_amounts_repayment_for_2_year(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=2)
        test_example.perform_repayment('equal_amounts')

        payment = test_example.get_payment()
        expenses = test_example.get_expenses()

        answer = 'Payment: 71000 - Expenses: 50000'
        self.assertEqual(answer, 'Payment: {:.0f} - Expenses: {:.0f}'.format(payment, expenses))

    def test_equal_amounts_repayment_for_3_year(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=3)
        test_example.perform_repayment('equal_amounts')

        payment = test_example.get_payment()
        expenses = test_example.get_expenses()

        answer = 'Payment: 64000 - Expenses: 50000'
        self.assertEqual(answer, 'Payment: {:.0f} - Expenses: {:.0f}'.format(payment, expenses))

    def test_equal_amounts_repayment_for_4_year(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=4)
        test_example.perform_repayment('equal_amounts')

        payment = test_example.get_payment()
        expenses = test_example.get_expenses()

        answer = 'Payment: 57000 - Expenses: 50000'
        self.assertEqual(answer, 'Payment: {} - Expenses: {}'.format(format(payment, '.0f'),
                                                                     format(expenses, '.0f')))


class TestEqualPaymentsRepaymentViewModel(unittest.TestCase):
    def test_equal_payments_repayment_for_1_year(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=1)
        test_example.perform_repayment('equal_payments')

        payment = test_example.get_payment()
        expenses = test_example.get_expenses()

        answer = 'Payment: 68641 - Expenses: 40641'
        self.assertEqual(answer, 'Payment: {} - Expenses: {}'.format(format(payment, '.0f'),
                                                                     format(expenses, '.0f')))

    def test_equal_payments_repayment_for_2_year(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=2)
        test_example.perform_repayment('equal_payments')

        payment = test_example.get_payment()
        expenses = test_example.get_expenses()

        answer = 'Payment: 68641 - Expenses: 46331'
        self.assertEqual(answer, 'Payment: {:.0f} - Expenses: {:.0f}'.format(payment, expenses))

    def test_equal_payments_repayment_for_3_year(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=3)
        test_example.perform_repayment('equal_payments')

        payment = test_example.get_payment()
        expenses = test_example.get_expenses()

        answer = 'Payment: 68641 - Expenses: 52817'
        self.assertEqual(answer, 'Payment: {:.0f} - Expenses: {:.0f}'.format(payment, expenses))

    def test_equal_payments_repayment_for_4_year(self):
        test_example = DebtViewModel(req_sum=200000, percent_rate=0.14, period=4, year=4)
        test_example.perform_repayment('equal_payments')

        payment = test_example.get_payment()
        expenses = test_example.get_expenses()

        answer = 'Payment: 68641 - Expenses: 60211'
        self.assertEqual(answer, 'Payment: {:.0f} - Expenses: {:.0f}'.format(payment, expenses))
