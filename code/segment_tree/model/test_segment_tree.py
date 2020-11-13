import unittest

from segment_tree.model.segment_tree import SegmentTree


class TestSegmentTree(unittest.TestCase):
    def test_cannot_create_tree_with_specific_type(self):
        with self.assertRaises(TypeError):
            SegmentTree('exp')

    def test_can_create_tree_only_with_list(self):
        with self.assertRaises(TypeError):
            array = {1: 2, 3: 4}

            tree = SegmentTree('sum')
            tree.build(array)

    def test_can_create_tree_only_with_list_of_integer(self):
        with self.assertRaises(TypeError):
            array = ['solo', 3, 2, 2]

            tree = SegmentTree('sum')
            tree.build(array)

    def test_sum_1(self):
        array = [4, 3, 2, 3, 4]

        tree = SegmentTree('sum')
        tree.build(array)

        self.assertEqual(tree.get(0, 4), sum(array))

    def test_sum_2(self):
        array = [4, 3, 2, 3, 4]

        tree = SegmentTree('sum')
        tree.build(array)

        self.assertEqual(tree.get(1, 3), sum(array[1:4]))

    def test_exception_if_right_index_is_lower_then_left(self):
        array = [4, 3, 2, 3, 4]

        tree = SegmentTree('sum')
        tree.build(array)

        with self.assertRaises(IndexError):
            tree.get(2, 0)

    def test_exception_if_index_is_greater_then_array_size(self):
        array = [4, 3, 2, 3, 4]

        tree = SegmentTree('sum')
        tree.build(array)

        with self.assertRaises(IndexError):
            tree.get(0, 8)

    def test_sum_after_update(self):
        array = [1, 3, 2, 5, 6]

        tree = SegmentTree('sum')
        tree.build(array)

        tree.update(index=1, new_value=0)

        self.assertEqual(tree.get(0, 4), sum(array) - 3)

    def test_exception_if_index_in_update_is_out_of_bounds(self):
        array = [1, 3, 2, 5, 6]

        tree = SegmentTree('sum')
        tree.build(array)

        with self.assertRaises(IndexError):
            tree.update(index=22, new_value=0)

    def test_max_1(self):
        array = [1, 0, 8]

        tree = SegmentTree('max')
        tree.build(array)

        self.assertEqual(tree.get(0, 2), 8)

    def test_max_2(self):
        array = [13, 5, 22, 5, 19, 4]

        tree = SegmentTree('max')
        tree.build(array)

        self.assertEqual(tree.get(3, 4), 19)

    def test_max_with_update(self):
        array = [1, 0, 8]

        tree = SegmentTree('max')
        tree.build(array)

        tree.update(index=1, new_value=15)

        self.assertEqual(tree.get(0, 2), 15)

    def test_min_1(self):
        array = [1, 0, 8]

        tree = SegmentTree('min')
        tree.build(array)

        self.assertEqual(tree.get(0, 2), 0)

    def test_min_2(self):
        array = [13, 5, 22, 5, 19, 4]

        tree = SegmentTree('min')
        tree.build(array)

        self.assertEqual(tree.get(3, 5), 4)

    def test_min_with_update(self):
        array = [13, 5, 22, 5, 19, 4]

        tree = SegmentTree('min')
        tree.build(array)

        tree.update(index=2, new_value=0)

        self.assertEqual(tree.get(2, 5), 0)
