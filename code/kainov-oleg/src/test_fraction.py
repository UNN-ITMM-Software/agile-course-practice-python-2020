import unittest

from fraction import Fraction, InvalidFractionError


class TestFractionClass(unittest.TestCase):
    def test_can_create_fraction(self):
        frac = Fraction()
        self.assertTrue(isinstance(frac, Fraction))

    def test_default_fraction_is_0_1(self):
        frac = Fraction()
        self.assertEqual(frac.p, 0)
        self.assertEqual(frac.q, 1)

    def test_can_create_1_2_fraction(self):
        frac = Fraction(1, 2)
        self.assertEqual(frac.p, 1)
        self.assertEqual(frac.q, 2)

    def test_cannot_create_x_0_fraction(self):
        with self.assertRaises(InvalidFractionError):
            Fraction(2, 0)

    def test_auto_reduce_fraction(self):
        frac = Fraction(2, 4)
        self.assertEqual(frac.p, 1)
        self.assertEqual(frac.q, 2)

    def test_multiply_fraction(self):
        frac_1 = Fraction(1, 3)
        frac_2 = Fraction(2, 5)
        result = frac_1 * frac_2
        self.assertEqual(result.p, 2)
        self.assertEqual(result.q, 15)

    def test_sum_fraction_1_2_1_2(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(1, 2)
        result = frac_1 + frac_2
        self.assertEqual(result.p, 1)
        self.assertEqual(result.q, 1)

    def test_sum_fraction_1_2_1_3(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(1, 3)
        result = frac_1 + frac_2
        self.assertEqual(result.p, 5)
        self.assertEqual(result.q, 6)

    def test_can_print_fraction(self):
        frac = Fraction(5, 7)
        self.assertEqual(str(frac), '5/7')
