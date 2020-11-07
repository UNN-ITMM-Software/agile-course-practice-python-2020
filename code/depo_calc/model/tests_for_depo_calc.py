import unittest

from depo_calc.model.depo_calc import Depo_calc

class TestDepoCelcClass(unittest.TestCase):
    def test_can_create_object(self):
        calc = Depo_calc()
        self.assertTrue(isinstance(calc, Depo_calc))

    def test_cant_create_invalid_object(self):
        with self.assertRaises(AssertionError):
            calc = Depo_calc(S0=-1, freq=9)

    def test_capitaliation_1(self):
        calc = Depo_calc(is_add_to_depo=True, freq=1)
        calc.capitalization()
        self.assertEqual(calc.income, 5)
        self.assertEqual(calc.S0, 105)

    def test_capitaliation_2(self):
        calc = Depo_calc(freq=1)
        calc.capitalization()
        self.assertEqual(calc.income, 5)
        self.assertEqual(calc.S0, 100)


    def test_revenue_1(self):
        calc = Depo_calc(freq=2, is_add_to_depo=True)
        self.assertEqual(calc.revenue(), 5.0625)
