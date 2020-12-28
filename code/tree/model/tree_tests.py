import unittest
from tree.model.tree import Tree


class TreeTestClass(unittest.TestCase):
    def test_create_normal(self):
        tree = Tree(1)
        self.assertIsInstance(tree, Tree)

    def test_create_invalid_data(self):
        with self.assertRaises(TypeError):
            Tree(0.5)

    def test_insert_valid_data(self):
        tree = Tree(10)
        tree.insert(5)
        self.assertEqual(5, tree.find_value(5))

    def test_insert_less_zero_data(self):
        tree = Tree(10)
        tree.insert(-5)
        self.assertEqual(-5, tree.find_value(-5))

    def test_insert_zero_data(self):
        tree = Tree(10)
        tree.insert(0)
        self.assertEqual(0, tree.find_value(0))

    def test_insert_invalid_data(self):
        with self.assertRaises(TypeError):
            Tree("g")

    def test_find_valid_data(self):
        tree = Tree(35)
        tree.insert(-79)
        tree.insert(0)
        tree.insert(16)
        self.assertEqual(16, tree.find_value(16))

    def test_find_invalid_data(self):
        with self.assertRaises(TypeError):
            Tree(-0.7)
     
    def test_get_tree(self):
        tree = Tree(35)
        tree.insert(-79)
        tree.insert(5)
        tree.insert(16)
        self.assertEqual([-79, 5, 16, 35], tree.get_tree())
