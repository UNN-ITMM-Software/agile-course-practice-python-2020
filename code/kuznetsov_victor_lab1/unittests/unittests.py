import unittest

from kuznetsov_victor_lab1.debt import DebtExpenses


class TestDebtExpensesClass(unittest.TestCase):
    def test_equal_amounts_repayment_with_invalid_req_sum(self):
        with self.assertRaises(ValueError):
            DebtExpenses(-333, 0.14, 4)

    def test_equal_amounts_repayment_with_invalid_percent_rate(self):
        with self.assertRaises(ValueError):
            DebtExpenses(200000, -0.14, 4)

    def test_equal_amounts_repayment_with_invalid_period(self):
        with self.assertRaises(ValueError):
            DebtExpenses(200000, 0.14, -4)

    def test_equal_amounts_repayment_with_all_invalid_values(self):
        with self.assertRaises(ValueError):
            DebtExpenses(-200000, -0.14, -4)

    def test_equal_amounts_repayment_with_invalid_type_req_sum(self):
        with self.assertRaises(TypeError):
            DebtExpenses(13823.4566, 0.14, 4)

    def test_equal_amounts_repayment_with_invalid_type_period(self):
        with self.assertRaises(TypeError):
            DebtExpenses(200000, 0.14, 4.5)

    def test_equal_amounts_repayment_with_invalid_type_percent_rate(self):
        with self.assertRaises(TypeError):
            DebtExpenses(200000, '0.14', 4)


class TestEqualAmountsRepayment(unittest.TestCase):
    def test_equal_amounts_repayment_for_1_year(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        payment, expenses = test_example.equal_amounts_repayment(1)
        self.assertEqual([format(payment, '.0f'), format(expenses, '.0f')], ['78000', '50000'])

    def test_equal_amounts_repayment_for_2_year(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        payment, expenses = test_example.equal_amounts_repayment(2)
        self.assertEqual([format(payment, '.0f'), format(expenses, '.0f')], ['71000', '50000'])

    def test_equal_amounts_repayment_for_3_year(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        payment, expenses = test_example.equal_amounts_repayment(3)
        self.assertEqual([format(payment, '.0f'), format(expenses, '.0f')], ['64000', '50000'])

    def test_equal_amounts_repayment_for_4_year(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        payment, expenses = test_example.equal_amounts_repayment(4)
        self.assertEqual([format(payment, '.0f'), format(expenses, '.0f')], ['57000', '50000'])

    def test_equal_amounts_repayment_for_all_years(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        req_sum = 0
        for i in range(1, 5, 1):
            _, expenses = test_example.equal_amounts_repayment(i)
            req_sum += expenses

        self.assertEqual(format(req_sum, '.0f'), '200000')

    def test_equal_amounts_repayment_for_invalid_pos_year(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        with self.assertRaises(Exception):
            test_example.equal_amounts_repayment(6)

    def test_equal_amounts_repayment_for_invalid_neg_year(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        with self.assertRaises(Exception):
            test_example.equal_amounts_repayment(-6)


class TestEqualPaymentsRepayment(unittest.TestCase):
    def test_equal_payments_repayment_for_1_year(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        payment, expenses = test_example.equal_payments_repayment(1)
        self.assertEqual([format(payment, '.0f'), format(expenses, '.0f')], ['68641', '40641'])

    def test_equal_payments_repayment_for_2_year(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        payment, expenses = test_example.equal_payments_repayment(2)
        self.assertEqual([format(payment, '.0f'), format(expenses, '.0f')], ['68641', '46331'])

    def test_equal_payments_repayment_for_3_year(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        payment, expenses = test_example.equal_payments_repayment(3)
        self.assertEqual([format(payment, '.0f'), format(expenses, '.0f')], ['68641', '52817'])

    def test_equal_payments_repayment_for_4_year(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        payment, expenses = test_example.equal_payments_repayment(4)
        self.assertEqual([format(payment, '.0f'), format(expenses, '.0f')], ['68641', '60211'])

    def test_equal_payments_repayment_for_all_years(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        req_sum = 0
        for i in range(1, 5, 1):
            _, expenses = test_example.equal_payments_repayment(i)
            req_sum += expenses

        self.assertEqual(format(req_sum, '.0f'), '200000')

    def test_equal_payments_repayment_for_invalid_pos_year(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        with self.assertRaises(Exception):
            test_example.equal_payments_repayment(6)

    def test_equal_payments_repayment_for_invalid_neg_year(self):
        test_example = DebtExpenses(200000, 0.14, 4)
        with self.assertRaises(Exception):
            test_example.equal_payments_repayment(-6)
