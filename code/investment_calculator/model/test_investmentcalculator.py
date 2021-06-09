import unittest

from investment_calculator.model.investmentcalculator import InvestmentCalculator, InvalidFormulaError


class TestInvestmentCalculator(unittest.TestCase):
    def test_can_create_formula_default(self):
        formula = InvestmentCalculator(100, 500, 10, 0.1)
        self.assertTrue(isinstance(formula, InvestmentCalculator))

    def test_can_create_formula_init_all(self):
        formula = InvestmentCalculator(100, 500, 10, 0.1)
        self.assertTrue(formula.R == 100 and formula.K == 500
                        and formula.n == 10 and formula.q == 0.1)

    def test_can_create_formula_neg_init_str(self):
        with self.assertRaises(InvalidFormulaError):
            InvestmentCalculator(K="abc")

    def test_can_create_formula_neg_init_list(self):
        with self.assertRaises(InvalidFormulaError):
            InvestmentCalculator([1, 2])

    def test_can_create_formula_neg_init_set(self):
        with self.assertRaises(InvalidFormulaError):
            InvestmentCalculator({1, 2})

    def test_can_create_formula_neg_init_bool(self):
        with self.assertRaises(InvalidFormulaError):
            InvestmentCalculator(K=True)

    def test_can_create_formula_neg_init_1(self):
        with self.assertRaises(InvalidFormulaError):
            InvestmentCalculator(K=-1)

    def test_can_create_formula_neg_init_0(self):
        with self.assertRaises(InvalidFormulaError):
            InvestmentCalculator(q=0)

    def test_calculate_formula_int(self):
        self.assertEqual(InvestmentCalculator(100, 500, 10, 1).calculate_net_present_value(), -400.09765625)

    def test_calculate_formula_float(self):
        self.assertEqual(InvestmentCalculator(100.1, 500.1, 10.1, 0.1).calculate_net_present_value(), 118.63198853578206)

    def test_can_add_K(self):
        formula = InvestmentCalculator(100, 500, 10, 0.1)
        formula.add_K(1)
        self.assertTrue(formula.K == 1)

    def test_can_add_R(self):
        formula = InvestmentCalculator(100, 500, 10, 0.1)
        formula.add_R(1)
        self.assertTrue(formula.R == 1)

    def test_can_add_q(self):
        formula = InvestmentCalculator(100, 500, 10, 0.1)
        formula.add_q(1)
        self.assertTrue(formula.q == 1)

    def test_can_add_n(self):
        formula = InvestmentCalculator(100, 500, 10, 0.1)
        formula.add_n(1)
        self.assertTrue(formula.n == 1)