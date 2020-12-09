import unittest

from segment_tree.viewmodel.viewmodel import SegmentTreeViewModel


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
