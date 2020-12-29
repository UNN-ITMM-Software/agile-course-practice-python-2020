import unittest

from ShutinaSvetlana.viewmodel.batcher_viewmodel import SortingViewModel
from ShutinaSvetlana.logger.fake_logger import FakeLogger


class TestSortingViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = SortingViewModel()

    def test_correct_input_num_check_btn_result(self):
        self.view_model.set_input_array('1 9 6 6 4 5 8 25')
        self.view_model.sort_btn_click()
        self.assertEqual('OK', self.view_model.get_sort_btn_clicked_result())

    def test_correct_sorting_numbers(self):
        self.view_model.set_input_array('1 9 6 6 4 5 8 25')
        self.view_model.sort_btn_click()
        self.assertEqual('1 4 5 6 6 8 9 25', self.view_model.get_sorted_array())

    def test_incorrect_input_check_btn_result1(self):
        self.view_model.set_input_array('1 9 a s 4 5 8 25')
        self.view_model.sort_btn_click()
        self.assertEqual('Error', self.view_model.get_sort_btn_clicked_result())

    def test_correct_input_char_check_btn_result(self):
        self.view_model.set_input_array('a s y f b')
        self.view_model.sort_btn_click()
        self.assertEqual('OK', self.view_model.get_sort_btn_clicked_result())

    def test_correct_sorting_characters(self):
        self.view_model.set_input_array('a s y f b')
        self.view_model.sort_btn_click()
        self.assertEqual('a b f s y', self.view_model.get_sorted_array())

    def test_incorrect_input_check_btn_result2(self):
        self.view_model.set_input_array('s d 1 5')
        self.view_model.sort_btn_click()
        self.assertEqual('Error', self.view_model.get_sort_btn_clicked_result())

    def test_correct_input_1_num_check_btn_result(self):
        self.view_model.set_input_array('9')
        self.view_model.sort_btn_click()
        self.assertEqual('OK', self.view_model.get_sort_btn_clicked_result())

    def test_correct_sorting_1_numb(self):
        self.view_model.set_input_array('9')
        self.view_model.sort_btn_click()
        self.assertEqual('9', self.view_model.get_sorted_array())

    def test_correct_input_float_num_check_btn_result(self):
        self.view_model.set_input_array('0.25 3.2 5.4 5')
        self.view_model.sort_btn_click()
        self.assertEqual('OK', self.view_model.get_sort_btn_clicked_result())

    def test_correct_sorting_float_numbers(self):
        self.view_model.set_input_array('0.25 3.2 5.4 5')
        self.view_model.sort_btn_click()
        self.assertEqual('0.25 3.2 5 5.4', self.view_model.get_sorted_array())

    def test_check_input_array(self):
        self.view_model.set_input_array('0.25 3.2 5.4 5')
        self.assertEqual('0.25 3.2 5.4 5', self.view_model.get_input_array())


class TestSortingViewModelFakeLogger(unittest.TestCase):

    def setUp(self):
        self.view_model = SortingViewModel(FakeLogger())

    def test_logger_check_input_array(self):
        self.view_model.set_input_array('0.25 3.2 5.4 5')
        self.assertEqual('Input array: 0.25 3.2 5.4 5', self.view_model.logger.get_last_log())

    def test_logger_check_success_result(self):
        self.view_model.set_input_array('0.25 3.2 5.4 5')
        self.view_model.sort_btn_click()
        self.assertEqual(['Input array: 0.25 3.2 5.4 5', 'Start reading the array',
                          'Start sorting', 'Sorting is OK', 'Result array: 0.25 3.2 5 5.4',
                          'Success'], self.view_model.get_logs())

    def test_logger_check_failed_result(self):
        self.view_model.set_input_array('s d 1 5')
        self.view_model.sort_btn_click()
        self.assertEqual(['Input array: s d 1 5', 'Start reading the array',
                          'Start sorting', 'Failed'], self.view_model.get_logs())
