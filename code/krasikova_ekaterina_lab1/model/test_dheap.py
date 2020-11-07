import unittest

from dheap import DHeap

class TestDHeap(unittest.TestCase):
    def test_can_create_dheap(self):
        dheap = DHeap(3)
        self.assertTrue(isinstance(dheap, DHeap))
