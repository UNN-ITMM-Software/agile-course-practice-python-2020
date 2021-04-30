import unittest

from radix.logger.fake_logger import FakeLogger
from radix.viewmodel.viewmodel import SortingViewModel


class TestSortingViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = SortingViewModel()

    def test_correct_input_num_check_btn_result(self):
        self.view_model.set_input_array('1 9 6 6 4 5 8 25')
        self.view_model.sort_btn_clicked()
        self.assertEqual('OK', self.view_model.get_sort_btn_clicked_result())

    def test_correct_sorting_numbers(self):
        self.view_model.set_input_array('1 9 6 6 4 5 8 25')
        self.view_model.sort_btn_clicked()
        self.assertEqual('1 4 5 6 6 8 9 25', self.view_model.get_sorted_array())

    def test_correct_handle_space(self):
        self.view_model.set_input_array(' 1 9 6 6 4 5 8 25')
        self.view_model.sort_btn_clicked()
        self.assertEqual('1 4 5 6 6 8 9 25', self.view_model.get_sorted_array())

    def test_incorrect_input_check_btn_result1(self):
        self.view_model.set_input_array('1 9 a s 4 5 8 25')
        self.view_model.sort_btn_clicked()
        self.assertEqual('Error', self.view_model.get_sort_btn_clicked_result())

    def test_incorrect_input_char_check_btn_result(self):
        self.view_model.set_input_array('a s y f b')
        self.view_model.sort_btn_clicked()
        self.assertEqual('Error', self.view_model.get_sort_btn_clicked_result())

    def test_incorrect_sorting_characters(self):
        self.view_model.set_input_array('a s y f b')
        self.view_model.sort_btn_clicked()
        self.assertEqual('Error', self.view_model.get_sort_btn_clicked_result())

    def test_incorrect_input_check_btn_result2(self):
        self.view_model.set_input_array('s d 1 5')
        self.view_model.sort_btn_clicked()
        self.assertEqual('Error', self.view_model.get_sort_btn_clicked_result())

    def test_correct_input_1_num_check_btn_result(self):
        self.view_model.set_input_array('9')
        self.view_model.sort_btn_clicked()
        self.assertEqual('OK', self.view_model.get_sort_btn_clicked_result())

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_sort_btn_state())

    def test_correct_sorting_1_numb(self):
        self.view_model.set_input_array('9')
        self.view_model.sort_btn_clicked()
        self.assertEqual('9', self.view_model.get_sorted_array())

    def test_incorrect_input_float_num_check_btn_result(self):
        self.view_model.set_input_array('0.25 3.2 5.4 5')
        self.view_model.sort_btn_clicked()
        self.assertEqual('Error', self.view_model.get_sort_btn_clicked_result())

    def test_incorrect_sorting_float_numbers(self):
        self.view_model.set_input_array('0.25 3.2 5.4 5')
        self.view_model.sort_btn_clicked()
        self.assertEqual('Error', self.view_model.get_sort_btn_clicked_result())

    def test_failed_check_input_array(self):
        self.view_model.set_input_array('0.25 3.2 5.4 5')
        self.assertEqual('0.25 3.2 5.4 5', self.view_model.get_input_array())


class TestSortingViewModelFakeLogger(unittest.TestCase):

    def setUp(self):
        self.view_model = SortingViewModel(FakeLogger())

    def test_logger_check_success_result(self):
        self.view_model.set_input_array('25 32 54 5')
        self.view_model.sort_btn_clicked()
        self.assertEqual(['Input array: 25 32 54 5', 'Start reading the array',
                          'Start sorting', 'Sorting is OK', 'Result array: 5 25 32 54',
                          'Success'], self.view_model.logger.get_logs())

    def test_logger_check_failed_result(self):
        self.view_model.set_input_array('s d 1 5')
        self.view_model.sort_btn_clicked()
        self.assertEqual(['Input array: s d 1 5', 'Start reading the array',
                          'Start sorting', 'Failed'], self.view_model.logger.get_logs())
