import unittest

from depo_calc.model.depo_calc import Depo_calc

class TestDepoCelcClass(unittest.TestCase):
    def test_can_create_object(self):
        calc = Depo_calc()
        self.assertTrue(isinstance(calc, Depo_calc))
