import unittest

from segment_tree.viewmodel.viewmodel import SegmentTreeViewModel
from segment_tree.logger.fakelogger import FakeLogger
from segment_tree.logger.reallogger import RealLogger


class TestSegmentTreeViewModel(unittest.TestCase):
    def test_create_view_model_object(self):
        test_view_model = SegmentTreeViewModel()
        self.assertEqual(SegmentTreeViewModel, type(test_view_model))

    def test_default_build_button_disable(self):
        test_view_model = SegmentTreeViewModel()
        self.assertEqual('disabled', test_view_model.is_build_button_enable())

    def test_default_get_button_disable(self):
        test_view_model = SegmentTreeViewModel()
        self.assertEqual('disabled', test_view_model.is_get_button_enable())

    def test_default_update_button_disable(self):
        test_view_model = SegmentTreeViewModel()
        self.assertEqual('disabled', test_view_model.is_update_button_enable())

    def test_build_button_enabled_after_input_array(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(4)
        self.assertEqual('normal', test_view_model.is_build_button_enable())

    def test_get_button_enabled_after_input_array(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_left_border(0)
        test_view_model.set_right_border(3)
        self.assertEqual('normal', test_view_model.is_get_button_enable())

    def test_update_button_enabled_after_input_array(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_array([1, 2, 3])
        test_view_model.set_update_index(0)
        test_view_model.set_update_value(3)
        self.assertEqual('normal', test_view_model.is_update_button_enable())

    def test_build_button_disable_value_error(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(-1)
        self.assertEqual('disabled', test_view_model.is_build_button_enable())

    def test_build_button_disable_type_error(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size('q')
        self.assertEqual('disabled', test_view_model.is_build_button_enable())

    def test_get_button_disable_left_border(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_left_border('-')
        test_view_model.set_right_border(3)
        self.assertEqual('disabled', test_view_model.is_get_button_enable())

    def test_get_button_disable_right_border(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_left_border(0)
        test_view_model.set_right_border('=')
        self.assertEqual('disabled', test_view_model.is_get_button_enable())

    def test_update_button_disable_wrong_index(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_update_index('a')
        test_view_model.set_update_value(2)
        self.assertEqual('disabled', test_view_model.is_update_button_enable())

    def test_update_button_disable_wrong_value(self):
        test_model = SegmentTreeViewModel()
        test_model.set_update_index(1)
        test_model.set_update_value('a')
        self.assertEqual('disabled', test_model.is_update_button_enable())

    def test_init_array_size(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        self.assertEqual(5, test_view_model.get_input_size())

    def test_init_wrong_value_array_size(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(-5)
        self.assertEqual('Incorrect value of input size', test_view_model.get_error_message())

    def test_init_wrong_type_array_size(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size('abc')
        self.assertEqual('Incorrect type of input size', test_view_model.get_error_message())

    def test_init_array(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_array([1, 2, 3])
        self.assertEqual([1, 2, 3], test_view_model.get_input_array())

    def test_init_wrong_array(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_array(1)
        self.assertEqual('Incorrect input array', test_view_model.get_error_message())

    def test_init_method(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_method('sum')
        self.assertEqual('sum', test_view_model.get_method())

    def test_init_left_border(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_left_border(0)
        self.assertEqual(0, test_view_model.get_left_border())

    def test_init_right_border(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_right_border(3)
        self.assertEqual(3, test_view_model.get_right_border())

    def test_init_wrong_left_border(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_left_border('abc')
        self.assertEqual('Incorrect left border', (test_view_model.get_error_message()))

    def test_init_wrong_right_border(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_right_border('abc')
        self.assertEqual('Incorrect right border', (test_view_model.get_error_message()))

    def test_init_update_index(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_update_index(3)
        self.assertEqual(3, test_view_model.get_update_index())

    def test_init_update_value(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_update_value(5)
        self.assertEqual(5, test_view_model.get_update_value())

    def test_init_update_wrong_index(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_update_index('-')
        self.assertEqual('Incorrect update index', test_view_model.get_error_message())

    def test_init_update_wrong_value(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_update_value('=')
        self.assertEqual('Incorrect update value', test_view_model.get_error_message())

    def test_calculate_sum_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('sum')
        test_view_model.calculate()
        self.assertEqual(True, test_view_model.get_success_procedure())

    def test_get_sum_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('sum')
        test_view_model.calculate()
        test_view_model.set_left_border(0)
        test_view_model.set_right_border(2)
        test_view_model.cut_array_for_given_border()
        self.assertEqual(25, test_view_model.get_calculate_result())

    def test_update_sum_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('sum')
        test_view_model.calculate()
        test_view_model.set_update_index(0)
        test_view_model.set_update_value(10)
        test_view_model.update()
        self.assertEqual(True, test_view_model.get_success_procedure())

    def test_calculate_max_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('max')
        test_view_model.calculate()
        self.assertEqual(True, test_view_model.get_success_procedure())

    def test_get_max_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('max')
        test_view_model.calculate()
        test_view_model.set_left_border(0)
        test_view_model.set_right_border(2)
        test_view_model.cut_array_for_given_border()
        self.assertEqual(17, test_view_model.get_calculate_result())

    def test_update_max_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('max')
        test_view_model.calculate()
        test_view_model.set_update_index(0)
        test_view_model.set_update_value(10)
        test_view_model.update()
        self.assertEqual(True, test_view_model.get_success_procedure())

    def test_calculate_min_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('min')
        test_view_model.calculate()
        self.assertEqual(True, test_view_model.get_success_procedure())

    def test_get_min_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('min')
        test_view_model.calculate()
        test_view_model.set_left_border(0)
        test_view_model.set_right_border(2)
        test_view_model.cut_array_for_given_border()
        self.assertEqual(2, test_view_model.get_calculate_result())

    def test_update_min_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('min')
        test_view_model.calculate()
        test_view_model.set_update_index(0)
        test_view_model.set_update_value(10)
        test_view_model.update()
        self.assertEqual(True, test_view_model.get_success_procedure())

    def test_except_message_calculate_sum_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 'a', 17, 3, 22])
        test_view_model.set_method('sum')
        test_view_model.calculate()
        self.assertEqual('Incorrect type of input array. Expected: list',
                         test_view_model.get_error_message())

    def test_except_status_calculate_sum_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 'a', 17, 3, 22])
        test_view_model.set_method('sum')
        test_view_model.calculate()
        self.assertEqual(False, test_view_model.get_success_procedure())

    def test_except_message_get_sum_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('sum')
        test_view_model.calculate()
        test_view_model.set_left_border(0)
        test_view_model.set_right_border(7)
        test_view_model.cut_array_for_given_border()
        self.assertEqual('Wrong indices: indices is out of bounds',
                         test_view_model.get_error_message())

    def test_except_status_get_sum_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('sum')
        test_view_model.calculate()
        test_view_model.set_left_border(0)
        test_view_model.set_right_border(7)
        test_view_model.cut_array_for_given_border()
        self.assertEqual(False, test_view_model.get_success_procedure())

    def test_except_message_update_sum_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('sum')
        test_view_model.calculate()
        test_view_model.set_update_index(-3)
        test_view_model.set_update_value(10)
        test_view_model.update()
        self.assertEqual('index is out of bounds', test_view_model.get_error_message())

    def test_except_status_update_sum_segment_tree(self):
        test_view_model = SegmentTreeViewModel()
        test_view_model.set_input_size(5)
        test_view_model.set_input_array([2, 6, 17, 3, 22])
        test_view_model.set_method('sum')
        test_view_model.calculate()
        test_view_model.set_update_index(-3)
        test_view_model.set_update_value(10)
        test_view_model.update()
        self.assertEqual(False, test_view_model.get_success_procedure())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = SegmentTreeViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome to segment tree application', self.view_model.logger.get_last_message())

    def test_logging_set_input_size(self):
        self.view_model.set_input_size(5)

        self.assertEqual('Set tree size = 5', self.view_model.logger.get_last_message())

    def test_logging_set_input_size_with_incorrect_argument(self):
        self.view_model.set_input_size('mistake')

        self.assertEqual('Incorrect type of input size', self.view_model.logger.get_last_message())

    def test_logging_set_input_array(self):
        self.view_model.set_input_array([1, 2, 3, 4, 5])

        self.assertEqual('Set array for tree [1, 2, 3, 4, 5]', self.view_model.logger.get_last_message())

    def test_logging_build_tree(self):
        self.view_model.set_input_size(5)
        self.view_model.set_input_array([1, 2, 3, 4, 5])
        self.view_model.set_method('sum')
        self.view_model.calculate()

        self.assertEqual('Build segment tree', self.view_model.logger.get_last_message())

    def test_logging_build_tree_failed(self):
        self.view_model.set_input_size(5)
        self.view_model.set_input_array([1, 2, 3, 4, 5])
        self.view_model.set_method('lol')
        self.view_model.calculate()

        self.assertEqual('Incorrect type of segment tree. Expected: max\min\sum',
                         self.view_model.logger.get_last_message())

    def test_logging_set_method(self):
        self.view_model.set_method('sum')

        self.assertEqual('Set method sum', self.view_model.logger.get_last_message())

    def test_logging_set_input_array_with_incorrect_argument(self):
        self.view_model.set_input_array(['mistake', 'mistake'])

        self.assertEqual('Incorrect input array', self.view_model.logger.get_last_message())

    def test_logging_set_left_border(self):
        self.view_model.set_left_border(0)

        self.assertEqual('Set left border = 0', self.view_model.logger.get_last_message())

    def test_logging_set_left_border_with_incorrect_argument(self):
        self.view_model.set_left_border('mistake')

        self.assertEqual('Incorrect left border', self.view_model.logger.get_last_message())

    def test_logging_set_right_border(self):
        self.view_model.set_right_border(2)

        self.assertEqual('Set right border = 2', self.view_model.logger.get_last_message())

    def test_logging_set_right_border_with_incorrect_argument(self):
        self.view_model.set_right_border('mistake')

        self.assertEqual('Incorrect right border', self.view_model.logger.get_last_message())

    def test_logging_set_update_index(self):
        self.view_model.set_update_index(1)

        self.assertEqual('Set update index = 1', self.view_model.logger.get_last_message())

    def test_logging_set_update_index_with_incorrect_argument(self):
        self.view_model.set_update_index('mistake')

        self.assertEqual('Incorrect update index', self.view_model.logger.get_last_message())

    def test_logging_set_update_value(self):
        self.view_model.set_update_value(100500)

        self.assertEqual('Set update value = 100500', self.view_model.logger.get_last_message())

    def test_logging_set_update_value_with_incorrect_argument(self):
        self.view_model.set_update_value('mistake')

        self.assertEqual('Incorrect update value', self.view_model.logger.get_last_message())

    def test_logging_update(self):
        self.view_model.set_input_size(5)
        self.view_model.set_input_array([1, 2, 3, 4, 5])
        self.view_model.set_method('sum')
        self.view_model.calculate()
        self.view_model.set_update_index(3)
        self.view_model.set_update_value(100500)
        self.view_model.update()

        self.assertEqual('Element updated', self.view_model.logger.get_last_message())

    def test_logging_update_failed(self):
        self.view_model.set_input_size(5)
        self.view_model.set_input_array([1, 2, 3, 4, 5])
        self.view_model.set_method('sum')
        self.view_model.calculate()
        self.view_model.set_update_index(10)
        self.view_model.set_update_value(100500)
        self.view_model.update()

        self.assertEqual('index is out of bounds', self.view_model.logger.get_last_message())

    def test_logging_cut_array(self):
        self.view_model.set_input_size(5)
        self.view_model.set_input_array([1, 2, 3, 4, 5])
        self.view_model.set_method('sum')
        self.view_model.calculate()
        self.view_model.set_left_border(0)
        self.view_model.set_right_border(2)
        self.view_model.cut_array_for_given_border()

        self.assertEqual('Cut array for given border, result: 6', self.view_model.logger.get_last_message())

    def test_logging_cut_array_fails(self):
        self.view_model.set_input_size(5)
        self.view_model.set_input_array([1, 2, 3, 4, 5])
        self.view_model.set_method('sum')
        self.view_model.calculate()
        self.view_model.set_left_border(-1)
        self.view_model.set_right_border(2)
        self.view_model.cut_array_for_given_border()

        self.assertEqual('Wrong indices: indices is out of bounds', self.view_model.logger.get_last_message())

    def test_logging_build_tree_full(self):
        expected_messages = ['Welcome to segment tree application',
                             'Set tree size = 5',
                             'Set array for tree [1, 2, 3, 4, 5]',
                             'Set method sum',
                             'Build segment tree']

        self.view_model.set_input_size(5)
        self.view_model.set_input_array([1, 2, 3, 4, 5])
        self.view_model.set_method('sum')
        self.view_model.calculate()

        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages())


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = SegmentTreeViewModel(RealLogger())
