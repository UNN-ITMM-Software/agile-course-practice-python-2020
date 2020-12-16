import unittest

from sorting.viewmodel.viewmodel import SortingViewModel


class TestSortingViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = SortingViewModel()

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_sort_btn_state())

    def test_when_entered_correct_input_array_button_enabled(self):
        self.view_model.set_input_array('1 9 6')
        self.assertNotEqual('disabled', self.view_model.get_sort_btn_state())

    def test_when_entered_wrong_input_array_button_disabled(self):
        self.view_model.set_input_array('1 a 6')
        self.assertEqual('disabled', self.view_model.get_sort_btn_state())

    def test_can_retrieve_input_array_text(self):
        self.view_model.set_input_array('1 9 6')
        input_array = self.view_model.get_input_array()
        self.assertEqual('1 9 6', input_array)

    def test_work_correctly_with_sorted_array(self):
        self.view_model.set_input_array('1 6 9')
        self.view_model.sort_btn_clicked()
        self.assertEqual('1.0 6.0 9.0', self.view_model.get_sorted_array())

    def test_sort_positive_int(self):
        self.view_model.set_input_array('1 9 6')
        self.view_model.sort_btn_clicked()
        self.assertEqual('1.0 6.0 9.0', self.view_model.get_sorted_array())

    def test_sort_positive_and_negative_int(self):
        self.view_model.set_input_array('1 -9 6')
        self.view_model.sort_btn_clicked()
        self.assertEqual('-9.0 1.0 6.0', self.view_model.get_sorted_array())

    def test_sort_float(self):
        self.view_model.set_input_array('1.5 9.1 6.8')
        self.view_model.sort_btn_clicked()
        self.assertEqual('1.5 6.8 9.1', self.view_model.get_sorted_array())
