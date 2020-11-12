import unittest

from mortgage_calculator.mortgage import Mortgage
from mortgage_calculator.term_types import TermType


class TestMortgage(unittest.TestCase):

    def test_create_calculator_with_term(self):
        Mortgage(5000000, 1500000, 5, term=1)

    def test_create_calculator_with_payment(self):
        Mortgage(5000000, 1500000, 5, monthly_payment=30000)

    def test_create_calculator_with_monthly_term(self):
        Mortgage(5000000, 1500000, 5, term=10, term_type=TermType.MONTHLY)

    def test_create_calculator_with_negative_amount(self):
        with self.assertRaises(ValueError):
            Mortgage(-10000, 0, 5)

    def test_create_calculator_with_big_initial_payment(self):
        with self.assertRaises(ValueError):
            Mortgage(10000, 20000, 5)

    def test_create_calculator_without_term_and_payment(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 20000, 5)

    def test_monthly_period_types(self):
        self.assertEquals(str(TermType.MONTHLY), "months")

    def test_yearly_period_types(self):
        self.assertEquals(str(TermType.YEARLY), "years")

    def test_period_types_not_equals(self):
        self.assertNotEquals(str(TermType.YEARLY), "months")

    def test_zero_payment_if_no_mortgage_amount(self):
        mortgage = Mortgage(2000000, 2000000, 5, term=10)
        self.assertEqual(mortgage.calculate_monthly_payment(), 0)

    def test_monthly_payment_calculation(self):
        mortgage = Mortgage(amount=2000000, initial_payment=500000, rate=5, term=10)
        self.assertEqual(mortgage.calculate_monthly_payment(), 15909.83)

    def test_monthly_payment_calculation_with_float_rate(self):
        mortgage = Mortgage(amount=5000000, initial_payment=2000000, rate=8.7, term=5)
        self.assertEqual(mortgage.calculate_monthly_payment(), 61839.18)

    def test_monthly_payment_calculation_for_monthly_mortgage(self):
        mortgage = Mortgage(amount=500000, initial_payment=200000, rate=8.7,
                            term=6, term_type=TermType.MONTHLY)
        self.assertEqual(mortgage.calculate_monthly_payment(), 51276.39)

    def test_monthly_payment_calculation_my_monthly_term(self):
        mortgage = Mortgage(amount=2000000, initial_payment=500000, rate=5,
                            term=120, term_type=TermType.MONTHLY)
        self.assertEqual(mortgage.calculate_monthly_payment(), 15909.83)

    def test_monthly_payment_calculation_equals_by_yearly_and_monthly_term_type(self):
        mortgage1 = Mortgage(amount=2000000, initial_payment=500000, rate=5,
                             term=5, term_type=TermType.YEARLY)
        mortgage2 = Mortgage(amount=2000000, initial_payment=500000, rate=5,
                             term=60, term_type=TermType.MONTHLY)
        self.assertEqual(mortgage1.calculate_monthly_payment(), mortgage2.calculate_monthly_payment())

    def test_monthly_payment_calculation_not_equal(self):
        mortgage1 = Mortgage(amount=2000000, initial_payment=500000, rate=5,
                             term=5, term_type=TermType.YEARLY)
        mortgage2 = Mortgage(amount=2000000, initial_payment=500000, rate=5,
                             term=5, term_type=TermType.MONTHLY)
        self.assertNotEqual(mortgage1.calculate_monthly_payment(), mortgage2.calculate_monthly_payment())

    def test_monthly_payment_with_no_term_specified(self):
        mortgage = Mortgage(2000000, 1000000, rate=5, monthly_payment=10000)
        self.assertEqual(mortgage.calculate_monthly_payment(), 10000)

    def test_term_calculation(self):
        mortgage = Mortgage(amount=2000000, initial_payment=500000, rate=5, monthly_payment=15910)
        self.assertEqual(mortgage.calculate_expected_term(), 120)

    def test_term_calculation_without_monthly_payment(self):
        with self.assertRaises(Exception):
            mortgage = Mortgage(2000000, 2000000, 5, term=5)
            mortgage.calculate_expected_term()

    def test_overpaid_amount_calculation(self):
        mortgage = Mortgage(5000000, 2000000, rate=8.7, term=5)
        self.assertEqual(mortgage.calculate_overpaid_amount(), 710350.8)

    def test_overpaid_amount_calculation_by_payment(self):
        mortgage = Mortgage(5000000, 2000000, rate=8.7, monthly_payment=61839)
        self.assertEqual(mortgage.calculate_overpaid_amount(), 710340)
