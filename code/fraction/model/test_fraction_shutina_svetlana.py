#!/usr/bin/env python
# coding: utf-8

import unittest

from fraction.model.fraction import Fraction, InvalidFractionError


class TestFractionClass(unittest.TestCase):
    def test_divide_fraction_3_4_3_4(self):
        frac_1 = Fraction(3, 4)
        frac_2 = Fraction(3, 4)
        result = frac_1 / frac_2
        self.assertTrue(result.is_equal(1, 1))

    def test_sum_negative_fraction_0_2_minus_1_3(self):
        frac_1 = Fraction(0, 2)
        frac_2 = Fraction(-1, 3)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(-1, 3))

    def test_sum_fraction_1_1_5_6(self):
        frac_1 = Fraction(1, 1)
        frac_2 = Fraction(5, 6)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(11, 6))

    def test_multiply_fraction_5_6_6_5(self):
        frac_1 = Fraction(5, 6)
        frac_2 = Fraction(6, 5)
        result = frac_1 * frac_2
        self.assertTrue(result.is_equal(1, 1))
