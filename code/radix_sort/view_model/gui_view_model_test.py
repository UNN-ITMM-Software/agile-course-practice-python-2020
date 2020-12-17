import unittest
from radix_sort.view_model.gui_view_model import RadixSortViewModel
from radix_sort.infrastructure.fake_logger import FakeLogger
from radix_sort.infrastructure.real_logger import RealLogger


class TestRadixSortViewModel(unittest.TestCase):
    def setUp(self):
        self.viewmodel = RadixSortViewModel()

    def test_sort_button_disable_state_default(self):
        self.assertEqual('disabled', self.viewmodel.get_sort_button_state())

    def test_sort_button_enable_state(self):
        self.viewmodel.set_input_data("1 3 5 2")
        self.assertEqual('active', self.viewmodel.get_sort_button_state())

    def test_set_correct_input_data(self):
        self.viewmodel.set_input_data("1 3 5 2")
        self.assertEqual("1 3 5 2", self.viewmodel.get_input_data())

    def test_sort_space_delimiter_array(self):
        self.viewmodel.set_input_data("1 3 5 2")
        self.viewmodel.start_sort()
        self.assertEqual("1, 2, 3, 5", self.viewmodel.get_output_data())

    def test_sort_empty_array(self):
        self.viewmodel.set_input_data("")
        self.viewmodel.start_sort()
        self.assertEqual("", self.viewmodel.get_output_data())

    def test_sort_comma_delimiter_array(self):
        self.viewmodel.set_input_data("1,3,5,2")
        self.viewmodel.start_sort()
        self.assertEqual("1, 2, 3, 5", self.viewmodel.get_output_data())

    def test_sort_comma_space_delimiter_array(self):
        self.viewmodel.set_input_data("1, 3,5 ,2")
        self.viewmodel.start_sort()
        self.assertEqual("1, 2, 3, 5", self.viewmodel.get_output_data())

    def test_sort_negative_array(self):
        self.viewmodel.set_input_data("-1,3,-5,-2")
        self.viewmodel.start_sort()
        self.assertEqual("-5, -2, -1, 3", self.viewmodel.get_output_data())

    def test_sort_string_array(self):
        self.viewmodel.set_input_data("a,s,5,g")
        self.viewmodel.start_sort()
        self.assertEqual("Incorrect input!", self.viewmodel.get_output_data())

    def test_sort_float_array(self):
        self.viewmodel.set_input_data("1.2,3.5,5.6,2.8")
        self.viewmodel.start_sort()
        self.assertEqual("Incorrect input!", self.viewmodel.get_output_data())


class TestRadixViewModelFakeLogger(unittest.TestCase):
    def setUp(self):
        self.viewmodel = RadixSortViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual(['Start Logging'], self.viewmodel.logger.get_last_messages(1))

    def test_logging_setting_input_data(self):
        self.viewmodel.set_input_data("1 3 5 2")
        input_data = self.viewmodel.get_input_data()
        self.assertEqual(['Getting input: ' + input_data], self.viewmodel.logger.get_last_messages(1))

    def test_logging_sorting(self):
        input_data = "1 3 5 2"
        self.viewmodel.set_input_data(input_data)
        self.viewmodel.start_sort()
        self.assertEqual(['Start Sorting: ' + input_data,
                         'Finish Sorting: ' + self.viewmodel.get_output_data()],
                         self.viewmodel.logger.get_last_messages(2))

    def test_logging_sorting_with_incorrect_input(self):
        input_data = "abc"
        self.viewmodel.set_input_data(input_data)
        self.viewmodel.start_sort()
        self.assertEqual(['Start Sorting: ' + input_data, 'Incorrect input: ' + input_data],
                         self.viewmodel.logger.get_last_messages(2))


class TestRadixViewModelRealLogger(TestRadixViewModelFakeLogger):
    def setUp(self):
        self.viewmodel = RadixSortViewModel(RealLogger())
