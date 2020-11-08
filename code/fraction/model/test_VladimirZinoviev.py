import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_create_fraction(self):
        try:
            Fraction()
        except Exception:
            self.fail('Can not create Fraction')

    def test_that_2_4_is_equal_1_2(self):
        frac = Fraction(2, 4)
        self.assertTrue(frac.is_equal(1, 2))
