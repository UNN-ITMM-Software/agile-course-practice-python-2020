import unittest

from fraction.model.fraction import Fraction


class TestFractionAgrishin(unittest.TestCase):
    def test_auto_reduce_fraction(self):
            frac = Fraction(2, 4)
            self.assertTrue(frac.is_equal(1, 2))

    def test_can_create_minus_1_2_fraction_with_rigth_pos(self):
        frac = Fraction(1, -2)
        self.assertTrue(frac.is_equal(-1, 2))
