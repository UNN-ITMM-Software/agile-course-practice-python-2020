import unittest

from galochkin_aleksei_lab_1.node import Node


class NodeTest(unittest.TestCase):

    def test_height(self):
        a = Node(1)
        self.assertEqual(1, Node.height(a))

    def test_height_2(self):
        a = Node(3)
        a = Node.insert(a, 2)
        self.assertEqual(2, Node.height(a))

    def test_insert_left(self):
        a = Node(3)
        a = Node.insert(a, 2)
        self.assertIsNotNone(a.left)
        self.assertIsNone(a.right)

    def test_insert_right(self):
        a = Node(3)
        a = Node.insert(a, 4)
        self.assertIsNotNone(a.right)
        self.assertIsNone(a.left)

    def test_insert_both_sides(self):
        a = Node(3)
        a = Node.insert(a, 4)
        a = Node.insert(a, 2)
        self.assertIsNotNone(a.right)
        self.assertIsNotNone(a.left)

    def test_rotate_right(self):
        a = Node(2)
        a = Node.insert(a, 1)
        a = Node.rotateright(a)
        self.assertEqual(1, a.key)
        self.assertEqual(2, a.right.key)

    def test_rotate_left(self):
        a = Node(1)
        a = Node.insert(a, 2)
        a = Node.rotateleft(a)
        self.assertEqual(2, a.key)
        self.assertEqual(1, a.left.key)

    def test_findmin(self):
        a = Node(5)
        for i in range(1, 4):
            a = Node.insert(a, i)
        for i in range(6, 9):
            a = Node.insert(a, i)
        self.assertEqual(1, Node.findmin(a).key)

    def test_removemin(self):
        a = Node(5)
        for i in range(1, 4):
            a = Node.insert(a, i)
        for i in range(6, 9):
            a = Node.insert(a, i)
        a = Node.removemin(a)
        self.assertEqual(2, Node.findmin(a).key)

    def test_contains_false(self):
        a = Node(1)
        for i in range(3, 9):
            a = Node.insert(a, i)
        self.assertEqual(False, Node.containskey(a, 2))

    def test_contains_true(self):
        a = Node(1)
        for i in range(3, 9):
            a = Node.insert(a, i)
        self.assertEqual(True, Node.containskey(a, 6))

    def test_remove(self):
        a = Node(1)
        for i in range(2, 9):
            a = Node.insert(a, i)
        self.assertEqual(True, Node.containskey(a, 5))
        a = Node.remove(a, 5)
        self.assertEqual(False, Node.containskey(a, 5))

    def test_remove_2(self):
        a = Node(1)
        for i in range(2, 9):
            a = Node.insert(a, i)
        self.assertEqual(True, Node.containskey(a, 6))
        a = Node.remove(a, 6)
        self.assertEqual(False, Node.containskey(a, 6))

    def test_bfactor(self):
        a = Node(1)
        a = Node.insert(a, 2)
        self.assertEquals(1, Node.bfactor(a))

    def test_fixheight(self):
        a = Node(1)
        a = Node.insert(a, 2)
        Node.fixheight(a)
        self.assertEqual(2, Node.height(a))

    def test_balance_right(self):
        a = Node(2)
        a.left = Node(1)
        a.right = Node(3)
        a.right.right = Node(4)
        Node.fixheight(a.right.right)
        Node.fixheight(a.right)
        Node.fixheight(a)
        Node.fixheight(a.left)
        Node.balance(a.right.right)
        self.assertEqual(1, Node.bfactor(a))

    def test_balance_left(self):
        a = Node(3)
        a.left = Node(2)
        a.left.left = Node(1)
        a.right = Node(4)
        Node.fixheight(a.left.left)
        Node.fixheight(a.left)
        Node.fixheight(a)
        Node.fixheight(a.right)
        Node.balance(a.left.left)
        self.assertEqual(-1, Node.bfactor(a))

    def test_balance(self):
        a = Node(2)
        a.left = Node(1)
        a.right = Node(3)
        a.right.right = Node(4)
        a.right.left = Node(5)
        a.right.height = 3
        a.left.height = 1
        a.right.right.height = 4
        a.right.left.height = 5
        Node.balance(a)
        self.assertEqual(-1, Node.bfactor(a))

    def test_remove_no_key(self):
        self.assertEqual(0, Node.remove(None, 3))
