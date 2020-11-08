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
    
    def test_raise_when_insert_element_of_non_numeric_type(self):
        dheap = DHeap(3)
        with self.assertRaises(TypeError):
            dheap.insert('t')

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

    def test_can_delete_min_of_3heap_with_3_elements(self):
        dheap = DHeap(3)
        dheap.insert(5)
        dheap.insert(3)
        dheap.insert(1)
        dheap_min = dheap.min()
        dheap.delete_min()
        self.assertTrue(dheap_min not in dheap.heap)
    
    def test_can_delete_min_of_4heap_with_10_elements_3_times(self):
        dheap = DHeap(4)
        for i in range(10, 0, -1):
            dheap.insert(i)
        for i in range(3):
            dheap_min = dheap.min()
            dheap.delete_min()
            self.assertTrue(dheap_min not in dheap.heap)

    def test_raise_when_delete_min_from_empty_heap(self):
        dheap = DHeap(4)
        with self.assertRaises(RuntimeError):
            dheap.delete_min()

    def test_can_decrease_weight_in_3heap_with_3_elements(self):
        dheap = DHeap(3)
        dheap.insert(5)
        dheap.insert(3)
        dheap.insert(1)
        dheap_min = dheap.min()
        dheap.decrease_weight(1, dheap.heap[1]-dheap_min+1)
        self.assertEqual(dheap.min(), 0)

    def test_can_decrease_weight_in_4heap_with_10_elements_10_times(self):
        dheap = DHeap(4)
        for i in range(10, 0, -1):
            dheap.insert(i)
        for i in range(10):
            dheap.decrease_weight(9, 2)
            self.assertEqual(dheap.min(), min(dheap.heap))
    
    def test_raise_when_increase_weight(self):
        dheap = DHeap(3)
        dheap.insert(5)
        dheap.insert(3)
        dheap.insert(1)
        with self.assertRaises(ValueError):
            dheap.decrease_weight(0, -4)
    
    def test_raise_when_decrease_weight_by_wrong_index(self):
        dheap = DHeap(3)
        dheap.insert(5)
        dheap.insert(3)
        dheap.insert(1)
        with self.assertRaises(ValueError):
            dheap.decrease_weight(5, 4)

    def test_can_delete_from_3heap_with_3_elements(self):
        dheap = DHeap(3)
        dheap.insert(5)
        dheap.insert(3)
        dheap.insert(1)
        dheap_elem_to_delete = dheap.heap[1]
        dheap.delete(1)
        self.assertTrue(dheap_elem_to_delete not in dheap.heap and dheap.min() == 1)

    def test_can_decrease_weight_in_4heap_with_10_elements_10_times(self):
        dheap = DHeap(4)
        for i in range(10, 0, -1):
            dheap.insert(i)
        for i in range(9):
            dheap_elem_to_delete = dheap.heap[1]
            dheap.delete(1)
            self.assertTrue(dheap_elem_to_delete not in dheap.heap and dheap.min() == 1)

    def test_raise_when_delete_by_wrong_index(self):
        dheap = DHeap(3)
        dheap.insert(5)
        dheap.insert(3)
        dheap.insert(1)
        with self.assertRaises(ValueError):
            dheap.delete(5)

    def test_can_create_3heap_with_3_elements_from_list(self):
        dheap = DHeap(3, [5, 1, 3])
        for i in range(3):
            self.assertEqual(dheap.min(), min(dheap.heap))
            dheap.delete_min()
    
    def test_can_create_4heap_with_10_elements_from_list(self):
        dheap = DHeap(4, list(range(10, 0, -1)))
        for i in range(10):
            self.assertEqual(dheap.min(), min(dheap.heap))
            dheap.delete_min()
        
    def test_raise_when_create_not_from_list(self):
        with self.assertRaises(TypeError):
            dheap = DHeap(3, {})

    def test_raise_when_create_from_list_with_non_numeric_type_of_elements(self):
        with self.assertRaises(TypeError):
            dheap = DHeap(3, ["t", "element"])
    
    def test_raise_when_set_value_of_d(self):
        dheap = DHeap(3)
        with self.assertRaises(AttributeError):
            dheap.d = 4
    
    def test_raise_when_set_value_of_heap(self):
        dheap = DHeap(3)
        with self.assertRaises(AttributeError):
            dheap.heap = [4, 5, 6]

    def test_can_get_d(self):
        dheap = DHeap(3, [5, 1, 3])
        self.assertEqual(dheap.d, 3)

    def test_can_get_copy_of_heap_list(self):
        dheap = DHeap(3, [5, 1, 3])
        heap = dheap.heap
        heap[0] = 12
        self.assertTrue(dheap.heap[0] != heap[0])
