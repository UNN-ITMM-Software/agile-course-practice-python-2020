import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):

    def test_can_create_3_5_fraction(self):
        frac = Fraction(3, 5)
        self.assertTrue(frac.is_equal(3, 5))

    def test_can_create_3_5_fraction_from_str(self):
        frac = Fraction.from_string('3/5')
        self.assertTrue(frac.is_equal(3, 5))
