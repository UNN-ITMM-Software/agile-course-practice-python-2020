import unittest

from dheap import DHeap

class TestDHeap(unittest.TestCase):
    def test_can_create_empty_3heap(self):
        dheap = DHeap(3)
        self.assertTrue(isinstance(dheap, DHeap))
    
    def test_can_insert_1_element_into_empty_3heap(self):
        dheap = DHeap(3)
        dheap.insert(5)
        self.assertEqual(dheap.heap, [5])

    def test_can_insert_2_elements_into_empty_3heap(self):
        dheap = DHeap(3)
        dheap.insert(5)
        dheap.insert(3)
        self.assertEqual(dheap.heap, [3, 5])

    def test_can_insert_3_elements_into_empty_3heap(self):
        dheap = DHeap(3)
        dheap.insert(5)
        dheap.insert(3)
        dheap.insert(1)
        self.assertTrue(dheap.heap[0] <= dheap.heap[1] and dheap.heap[0] <= dheap.heap[2])

    def test_can_get_min_of_3heap_with_1_element(self):
        dheap = DHeap(3)
        dheap.insert(5)
        self.assertEqual(dheap.min(), 5)
    
    def test_can_get_min_of_3heap_with_3_elements(self):
        dheap = DHeap(3)
        dheap.insert(5)
        dheap.insert(3)
        dheap.insert(1)
        self.assertEqual(dheap.min(), 1)

    def test_can_get_min_of_4heap_with_10_elements(self):
        dheap = DHeap(4)
        for i in range(10, 0, -1):
            dheap.insert(i)
        self.assertEqual(dheap.min(), 1)
