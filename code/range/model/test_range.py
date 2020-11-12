import unittest

from range.model.range import Range


class TestRange(unittest.TestCase):
    def test_can_create(self):
        range_object = Range('[1,3]')
        self.assertTrue(isinstance(range_object, Range))

    def test_cant_create_from_empty_str(self):
        with self.assertRaises(ValueError):
            Range('')

    def test_cant_create_empty_range(self):
        with self.assertRaises(ValueError):
            Range('(1,2)')

    def test_cant_create_reversed_range(self):
        with self.assertRaises(ValueError):
            Range('(6,2)')

    def test_can_create_one_elem_range(self):
        range_object = Range('[3,3]')
        self.assertTrue(isinstance(range_object, Range))

    def test_can_create_with_left_parenthesis(self):
        range_object = Range('(1,3]')
        self.assertTrue(isinstance(range_object, Range))

    def test_can_create_with_right_parenthesis(self):
        range_object = Range('[1,3)')
        self.assertTrue(isinstance(range_object, Range))

    def test_can_create_with_both_parentheses(self):
        range_object = Range('(1,3)')
        self.assertTrue(isinstance(range_object, Range))

    def test_can_create_with_left_square(self):
        range_object = Range('[1,3)')
        self.assertTrue(isinstance(range_object, Range))

    def test_can_create_with_right_square(self):
        range_object = Range('(1,3]')
        self.assertTrue(isinstance(range_object, Range))

    def test_can_create_with_both_squares(self):
        range_object = Range('[1,3]')
        self.assertTrue(isinstance(range_object, Range))

    def test_can_create_with_negatives(self):
        range_object = Range('[-1,3]')
        self.assertTrue(isinstance(range_object, Range))

    def test_not_contain_border_element_with_parenthesis(self):
        range_object = Range('(-1,3]')
        self.assertFalse(range_object.contains_value(-1))

    def test_not_contain_value(self):
        range_object = Range('(-1,3]')
        self.assertFalse(range_object.contains_value(99))

    def test_contain_border_element_with_quarter(self):
        range_object = Range('(-1,3]')
        self.assertTrue(range_object.contains_value(3))

    def test_contain_wrong_type_error(self):
        range_object = Range('(-1,3]')
        value = 'a'
        with self.assertRaises(TypeError):
            range_object.contains_value(value)

    def test_contain_set(self):
        range_object = Range('(-1,3]')
        values = [0, 2, 3]
        self.assertTrue(range_object.contains_set(values))

    def test_wrong_type_contain_set(self):
        range_object = Range('(-1,3]')
        value = 'type-error'
        with self.assertRaises(TypeError):
            range_object.contains_set(value)

    def test_not_contain_set(self):
        range_object = Range('(-1,3]')
        values = [0, 2, 3, 99]
        self.assertFalse(range_object.contains_set(values))

    def test_get_all_points(self):
        range_object = Range('(-1,3]')
        values = [0, 1, 2, 3]
        self.assertEqual(range_object.get_all_points(), values)

    def test_contain_range(self):
        range_object = Range('(-1,4]')
        value = Range('[0,2]')
        self.assertTrue(range_object.contains_range(value))

    def test_contain_range_wrong_type_error(self):
        range_object = Range('(-1,3]')
        value = 'a'
        with self.assertRaises(TypeError):
            range_object.contains_set(value)

    def test_not_contain_range(self):
        range_object = Range('(-1,4]')
        value = Range('[5,20]')
        self.assertFalse(range_object.contains_range(value))

    def test_overlaps_wrong_type_error(self):
        range_object = Range('(-1,3]')
        value = 'a'
        with self.assertRaises(TypeError):
            range_object.overlaps_range(value)

    def test_overlaps(self):
        range_object = Range('(-1,4]')
        value = Range('[-1,20]')
        self.assertTrue(range_object.overlaps_range(value))

    def test_not_overlaps(self):
        range_object = Range('(-1,4]')
        value = Range('(5,20]')
        self.assertFalse(range_object.overlaps_range(value))

    def test_equals_wrong_type_error(self):
        range_object = Range('(-1,3]')
        value = 'a'
        with self.assertRaises(TypeError):
            range_object.equals(value)

    def test_equal(self):
        range_object = Range('(-1,4]')
        value = Range('(-1,4]')
        self.assertTrue(range_object.equals(value))

    def test_equal_diff_brackets(self):
        range_object = Range('(-1,4]')
        value = Range('[0,5)')
        self.assertTrue(range_object.equals(value))

    def test_not_equal(self):
        range_object = Range('(-1,4]')
        value = Range('(-5,4]')
        self.assertFalse(range_object.equals(value))

    def test_end_points(self):
        range_object = Range('(-1,4]')
        end_points = [0, 4]
        self.assertEqual(range_object.end_points(), end_points)
