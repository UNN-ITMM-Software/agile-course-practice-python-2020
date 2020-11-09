import unittest

from deposit_calc.model.deposit_calc import DepositCalc


class TestDepoCelcClass(unittest.TestCase):
    def test_can_create_object(self):
        calc = DepositCalc()
        self.assertTrue(isinstance(calc, DepositCalc))

    def test_cant_create_invalid_object_1(self):
        with self.assertRaises(AssertionError):
            DepositCalc(s0=-1, capitalization_freq=9)

    def test_capitaliation_1(self):
        calc = DepositCalc(is_add_to_depo=True, capitalization_freq=1)
        calc.capitalization()
        self.assertEqual(calc.income, 5)
        self.assertEqual(calc.s0, 105)

    def test_capitaliation_2(self):
        calc = DepositCalc(capitalization_freq=1)
        calc.capitalization()
        self.assertEqual(calc.income, 5)
        self.assertEqual(calc.s0, 100)

    def test_can_replenish(self):
        calc = DepositCalc(capitalization_freq=4, replenishment_freq=2)
        calc.replenishment(10)
        calc.replenishment(20)
        self.assertEqual(calc.s0, 130)

    def test_cant_replenish_negative_value(self):
        calc = DepositCalc(capitalization_freq=2, replenishment_freq=1)
        with self.assertRaises(AssertionError):
            calc.replenishment(-10)

    def test_revenue_1(self):
        calc = DepositCalc(capitalization_freq=2, is_add_to_depo=True)
        self.assertEqual(calc.revenue(), 5)

    def test_revenue_2(self):
        calc = DepositCalc(s0=100000, capitalization_freq=4, replenishment_freq=2, is_add_to_depo=True)
        self.assertEqual(calc.revenue(values=[10000, 10000]), 5346)

    def test_revenue_3(self):
        calc = DepositCalc(t=1.5, s0=100000, capitalization_freq=4, replenishment_freq=2, is_add_to_depo=True)
        self.assertEqual(calc.revenue(values=[10000, 10000, 10000]), 8499)

    def test_revenue_no_add_to_depo(self):
        calc = DepositCalc(s0=100000, capitalization_freq=4, replenishment_freq=2, is_add_to_depo=False)
        calc.revenue(values=[10000, 10000])
        self.assertEqual(calc.income, 5250)

    def test_cant_create_invalid_object_2(self):
        with self.assertRaises(AssertionError):
            DepositCalc(capitalization_freq=1, replenishment_freq=2)

    def test_can_print_data(self):
        calc = DepositCalc(s0=10000, capitalization_freq=1)
        calc.revenue()
        s, r, i = calc.get_data()
        self.assertEqual(s, 10000)
        self.assertEqual(r, 0)
        self.assertEqual(i, 500)
