import unittest

from complex_calc.viewmodel.complex_viewmodel import ComplexNumViewModel


class TestComplexNumCalculatorViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = ComplexNumViewModel()

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_both_complex_nums_button_enabled(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1+2i')
        self.assertNotEqual('disabled', self.view_model.get_button_convert_state())

    def test_can_retrieve_complex_nums_text(self):
        self.view_model.set_first_complex_num(' 1+1i')
        self.view_model.set_second_complex_num('1+2i')
        actual_c_n_1 = self.view_model.get_first_complex_num()
        actual_c_n_2 = self.view_model.get_second_complex_num()

        self.assertEqual('1+1i', actual_c_n_1)
        self.assertEqual('1+2i', actual_c_n_2)

    def test_when_entered_both_complex_nums_then_clear_one_button_disabled(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1+2i')
        self.view_model.set_first_complex_num('')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_not_complex_num_button_disabled(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1a')
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_can_add_11_and_12(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1+2i')
        self.view_model.click_convert()
        self.assertEqual('2.0 + 3.0i', self.view_model.get_answer_text())

    def test_can_add_11_and_1(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1')
        self.view_model.click_convert()
        self.assertEqual('2.0 + 1.0i', self.view_model.get_answer_text())

    def test_can_add_11_and_1_neg1(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1-1i')
        self.view_model.click_convert()
        self.assertEqual('2.0 + 0.0i', self.view_model.get_answer_text())

    def test_can_sub_11_and_12(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1+2i')
        self.view_model.set_operation('-')
        self.view_model.click_convert()
        self.assertEqual('0.0 - 1.0i', self.view_model.get_answer_text())

    def test_can_sub_11_and_1(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1')
        self.view_model.set_operation('-')
        self.view_model.click_convert()
        self.assertEqual('0.0 + 1.0i', self.view_model.get_answer_text())

    def test_can_sub_11_and_1_neg1(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1-1i')
        self.view_model.set_operation('-')
        self.view_model.click_convert()
        self.assertEqual('0.0 + 2.0i', self.view_model.get_answer_text())

    def test_can_mul_11_and_12(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1+2i')
        self.view_model.set_operation('*')
        self.view_model.click_convert()
        self.assertEqual('-1.0 + 3.0i', self.view_model.get_answer_text())

    def test_can_mul_11_and_1(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1')
        self.view_model.set_operation('*')
        self.view_model.click_convert()
        self.assertEqual('1.0 + 1.0i', self.view_model.get_answer_text())

    def test_can_mul_11_and_1_neg1(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1-1i')
        self.view_model.set_operation('*')
        self.view_model.click_convert()
        self.assertEqual('2.0 + 0.0i', self.view_model.get_answer_text())

    def test_div_11_and_12(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1+2i')
        self.view_model.set_operation('/')
        self.view_model.click_convert()
        str_c_n = ''.join(self.view_model.get_answer_text().split()).replace('i', 'j')
        c_n = complex(str_c_n)
        self.assertTrue(abs(c_n.real - 0.6) < 1e-10 and abs(c_n.imag + 0.2) < 1e-10)

    def test_can_div_11_and_1(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1')
        self.view_model.set_operation('/')
        self.view_model.click_convert()
        self.assertEqual('1.0 + 1.0i', self.view_model.get_answer_text())

    def test_can_div_11_and_1_neg1(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1-1i')
        self.view_model.set_operation('/')
        self.view_model.click_convert()
        str_c_n = ''.join(self.view_model.get_answer_text().split()).replace('i', 'j')
        c_n = complex(str_c_n)
        self.assertTrue(abs(c_n.real - 0.0) < 1e-10 and abs(c_n.imag - 1.0) < 1e-10)

    def test_can_div_11_and_0(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('0')
        self.view_model.set_operation('/')
        self.view_model.click_convert()
        self.assertEqual('Error! Cannot divide by zero!', self.view_model.get_answer_text())

    def test_can_eq_11_and_11(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1+1i')
        self.view_model.set_operation('==')
        self.view_model.click_convert()
        self.assertEqual('True', self.view_model.get_answer_text())

    def test_can_eq_11_and_1(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1')
        self.view_model.set_operation('==')
        self.view_model.click_convert()
        self.assertEqual('False', self.view_model.get_answer_text())

    def test_can_not_eq_11_and_11(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1+1i')
        self.view_model.set_operation('!=')
        self.view_model.click_convert()
        self.assertEqual('False', self.view_model.get_answer_text())

    def test_can_not_eq_11_and_1(self):
        self.view_model.set_first_complex_num('1+1i')
        self.view_model.set_second_complex_num('1')
        self.view_model.set_operation('!=')
        self.view_model.click_convert()
        self.assertEqual('True', self.view_model.get_answer_text())
