import unittest as ut
from radix_sort.view_model.gui_view_model import RadixSortViewModel


class MyTestCase(ut.TestCase):
    def setUp(self):
        self.model = RadixSortViewModel()

    def test_sort_button_disable_state_default(self):
        self.assertEqual('disabled', self.model.get_sort_button_state())

    def test_sort_button_enable_state(self):
        self.model.set_input_data("1 3 5 2")
        self.assertEqual('active', self.model.get_sort_button_state())

    def test_set_correct_input_data(self):
        self.model.set_input_data("1 3 5 2")
        self.assertEqual("1 3 5 2", self.model.get_input_data())

    def test_sort_space_delimiter_array(self):
        self.model.set_input_data("1 3 5 2")
        self.model.start_sort()
        self.assertEqual("1 2 3 5", self.model.get_output_data())

    def test_sort_empty_array(self):
        self.model.set_input_data("")
        self.model.start_sort()
        self.assertEqual("", self.model.get_output_data())

    def test_sort_comma_delimiter_array(self):
        self.model.set_input_data("1,3,5,2")
        self.model.start_sort()
        self.assertEqual("1 2 3 5", self.model.get_output_data())

    def test_sort_comma_space_delimiter_array(self):
        self.model.set_input_data("1, 3,5 ,2")
        self.model.start_sort()
        self.assertEqual("1 2 3 5", self.model.get_output_data())

    def test_sort_negative_array(self):
        self.model.set_input_data("-1,3,-5,-2")
        self.model.start_sort()
        self.assertEqual("-5 -2 -1 3", self.model.get_output_data())

    def test_sort_string_array(self):
        self.model.set_input_data("a,s,5,g")
        self.model.start_sort()
        self.assertEqual("Please, check correct input data", self.model.get_output_data())

    def test_sort_float_array(self):
        self.model.set_input_data("1.2,3.5,5.6,2.8")
        self.model.start_sort()
        self.assertEqual("Please, check correct input data", self.model.get_output_data())
