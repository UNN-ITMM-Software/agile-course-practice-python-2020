import unittest

from range.viewmodel.operation import Operation
from range.viewmodel.viewmodel import RangeViewModel


class TestRangeViewModel(unittest.TestCase):

    def test_can_set_operation(self):
        rang = RangeViewModel()
        rang.set_operation(operation=Operation.EQUALS)
        self.assertEqual(rang.get_operation(), Operation.EQUALS)

    def test_can_change_value_2_enable(self):
        rang = RangeViewModel()
        rang.set_operation(operation=Operation.EQUALS)
        res = rang.get_value_2_enabled()
        self.assertTrue(res)

    def test_get_empty_value_1(self):
        rang = RangeViewModel()
        self.assertEqual(rang.get_value_1_string(), '')

    def test_set_value_1(self):
        rang = RangeViewModel()
        rang.set_value_1('[1,3]')
        self.assertEqual(rang.get_value_1_string(), '[1,3]')

    def test_set_value_1_wrong_format(self):
        rang = RangeViewModel()
        with self.assertRaises(ValueError):
            rang.set_value_1('[1, 3]')

    def test_set_value_1_range_with_incorrect_end_points(self):
        rang = RangeViewModel()
        with self.assertRaises(ValueError):
            rang.set_value_1('[3, 1]')

    def test_get_empty_value_2(self):
        rang = RangeViewModel()
        self.assertEqual(rang.get_value_2_string(), '')

    def test_set_num_to_value_2(self):
        rang = RangeViewModel()
        rang.set_value_2('4')
        self.assertEqual(rang.get_value_2_string(), '4')

    def test_set_range_to_value_2(self):
        rang = RangeViewModel()
        rang.set_value_2('[1,3]')
        self.assertEqual(rang.get_value_2_string(), '[1,3]')

    def test_set_list_to_value_2(self):
        rang = RangeViewModel()
        rang.set_value_2('1,3')
        self.assertEqual(rang.get_value_2_string(), '1, 3')

    def test_set_list_with_spaces_to_value_2(self):
        rang = RangeViewModel()
        rang.set_value_2('1 3')
        self.assertEqual(rang.get_value_2_string(), '1, 3')

    def test_set_invalid_value_to_value_2(self):
        rang = RangeViewModel()
        with self.assertRaises(TypeError):
            rang.set_value_2('abc')

    def test_make_contains_operation_with_num(self):
        rang = RangeViewModel()
        rang.set_value_1('[1,3]')
        rang.set_value_2('4')
        rang.make_operation()
        self.assertEqual(rang.get_result_string(), 'No')

    def test_make_contains_operation_with_list(self):
        rang = RangeViewModel()
        rang.set_value_1('[1,5]')
        rang.set_value_2('2, 3')
        rang.make_operation()
        self.assertEqual(rang.get_result_string(), 'Yes')

    def test_make_contains_operation_with_range(self):
        rang = RangeViewModel()
        rang.set_value_1('[1,5]')
        rang.set_value_2('[1,3]')
        rang.make_operation()
        self.assertEqual(rang.get_result_string(), 'Yes')

    def test_overlap_operation(self):
        rang = RangeViewModel()
        rang.set_operation(Operation.OVERLAP)
        rang.set_value_1('[1,5]')
        rang.set_value_2('[2,3]')
        rang.make_operation()
        self.assertEqual(rang.get_result_string(), 'No')

    def test_equals_operation(self):
        rang = RangeViewModel()
        rang.set_operation(Operation.EQUALS)
        rang.set_value_1('[1,5]')
        rang.set_value_2('[1,5)')
        rang.make_operation()
        self.assertEqual(rang.get_result_string(), 'No')

    def test_get_all_points_operation(self):
        rang = RangeViewModel()
        rang.set_operation(Operation.ALL_POINTS)
        rang.set_value_1('(1,5]')
        rang.make_operation()
        self.assertEqual(rang.get_result_string(), '2 3 4 5')

    def test_get_end_points_operation(self):
        rang = RangeViewModel()
        rang.set_operation(Operation.END_POINTS)
        rang.set_value_1('(1,5)')
        rang.make_operation()
        self.assertEqual(rang.get_result_string(), '2 4')

    def test_get_result_string(self):
        rang = RangeViewModel()
        self.assertEqual(rang.get_result_string(), '')

    def test_clear_result(self):
        rang = RangeViewModel()
        rang.set_value_1('(1,5)')
        rang.set_operation(Operation.END_POINTS)
        rang.make_operation()
        rang.clear_result()
        self.assertEqual(rang.get_result_string(), '')
