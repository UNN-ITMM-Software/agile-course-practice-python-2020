import unittest

from polynomial_calculator.viewmodel.viewmodel_polynomial_calculator import PolyViewModel


class TestPolyViewModel(unittest.TestCase):

    # INIT TESTS

    def test_init_first_poly(self):
        t = PolyViewModel()
        t.set_first_poly('1,2,3')
        self.assertEqual('1,2,3', t.get_first_poly())

    def test_init_second_poly(self):
        t = PolyViewModel()
        t.set_second_poly('1,2,3')
        self.assertEqual('1,2,3', t.get_second_poly())

    def test_init_operation(self):
        t = PolyViewModel()
        t.set_operation('-')
        self.assertEqual('-', t.get_operation())

    # COMPUTING TESTS

    def test_computing_add(self):
        t = PolyViewModel()
        t.set_first_poly('1,2,3')
        t.set_second_poly('4,5,6,7')
        t.set_operation('+')
        t.computing()
        self.assertEqual('4x^3 + 6x^2 + 8x + 10', t.get_result())

    def test_computing_sub(self):
        t = PolyViewModel()
        t.set_first_poly('1,2,3')
        t.set_second_poly('4,5,6,7')
        t.set_operation('-')
        t.computing()
        self.assertEqual('-4x^3 + -4x^2 + -4x + -4', t.get_result())

    def test_computing_with_er_val(self):
        t = PolyViewModel()
        t.set_first_poly('1,2,3,a')
        t.set_second_poly('4,5,6,7')
        t.set_operation('-')
        t.computing()
        self.assertEqual('Coeff has no type int', t.get_result())

    def test_computing_composition(self):
        t = PolyViewModel()
        t.set_first_poly('1,2,3')
        t.set_second_poly('4,5,6,7')
        t.set_operation('*')
        t.computing()
        self.assertEqual('4x^5 + 13x^4 + 28x^3 + 34x^2 + 32x + 21', t.get_result())
