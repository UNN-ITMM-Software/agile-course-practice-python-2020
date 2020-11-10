import unittest
import random
from .fibonacci_heap import FibonacciHeap

RANDOM_SEED = 1


class TestHeaps(unittest.TestCase):
    """
    Test methods of the Fibonacci heap
    """
    def insert_key_test(self, heap: 'FibonacciHeap'):
        """
        testing the insert() work

        :param heap: the testing heap
        """
        for k in [-10, 0, 10, -1.1, 1.1]:
            n = heap.insert(k)
            self.assertEqual(n.key, k)
            self.assertEqual(n.val, k)

    def insert_key_value_test(self, heap: 'FibonacciHeap'):
        """
        testing the insert() support parameter .val properly

        :param heap: the testing heap
        """
        for k, v in [(-10, 0), (0, "A"), (10, [1, 2]), (-1.1, {}), (1.1, 1.1)]:
            n = heap.insert(k, v)
            self.assertEqual(n.key, k)
            self.assertEqual(n.val, v)

    def find_min_test(self, heap: 'FibonacciHeap'):
        """
        testing the find_min(), should return the min node
        :param heap: the testing heap
        """
        random.seed(RANDOM_SEED)
        keys = random.sample(range(-1000, 1000), 100)
        added_keys = []
        for k in keys:
            added_keys.append(k)
            heap.insert(k)
            self.assertEqual(heap.find_min().key, min(added_keys))

    def delete_min_test(self, heap: 'FibonacciHeap'):
        """
        testing the delete_min() deleting the min node

        :param heap: the testing heap
        """
        random.seed(RANDOM_SEED)
        keys = random.sample(range(-1000, 1000), 100)
        for k in keys:
            heap.insert(k)
        keys = sorted(keys)

        while len(keys) > 0:
            min_key = keys.pop(0)
            heap_min = heap.delete_min()
            self.assertEqual(heap_min.key, min_key)

    def delete_test(self, heap: 'FibonacciHeap'):
        """
        testing the delete() works
        and find_min() returns min node

        :param heap: the testing heap
        """
        random.seed(RANDOM_SEED)
        keys = random.sample(range(-1000, 1000), 100)
        nodes = []
        for k in keys:
            nodes.append(heap.insert(k))

        while len(nodes) > 1:
            node = nodes.pop(random.randrange(len(nodes)))
            heap.delete(node)
            self.assertEqual(heap.find_min(), min(nodes, key=lambda n: n.key))

    def decrease_key_test(self, heap: 'FibonacciHeap'):
        """
        testing the decrease_key() works
        and find_min() returns correct min node

        :param heap: the testing heap
        """
        random.seed(RANDOM_SEED)
        keys = random.sample(range(-1000, 1000), 100)
        nodes = []
        for k in keys:
            nodes.append(heap.insert(k))

        for _ in range(100):
            index = random.randrange(len(nodes))
            key_new = nodes[index].key - random.randint(1, 1000)
            nodes[index] = heap.decrease_key(nodes[index], key_new)
            self.assertEqual(nodes[index].key, key_new)
            self.assertEqual(heap.find_min(), min(nodes, key=lambda n: n.key))

    def merge_test(self, heap: 'FibonacciHeap'):
        """
        testing the merge() works, and find_min() returns correct min node

        :param heap: the testing heap
        """
        first_heap = heap
        random.seed(RANDOM_SEED)

        first_heap.insert(1)
        all_keys = [1]
        for _ in range(10):
            new_heap = heap
            keys = random.sample(range(-1000, 1000), 100)
            for k in keys:
                new_heap.insert(k)

            first_heap.merge(new_heap)
            all_keys.extend(keys)
            self.assertEqual(first_heap.find_min().key, min(all_keys))

    def test_heap_insert(self):
        self.insert_key_test(heap=FibonacciHeap())
        self.insert_key_value_test(heap=FibonacciHeap())

    def test_heap_find_min(self):
        self.find_min_test(heap=FibonacciHeap())

    def test_heap_delete_min(self):
        self.delete_min_test(heap=FibonacciHeap())

    def test_heap_delete(self):
        self.delete_test(heap=FibonacciHeap())

    def test_heap_decrease_key(self):
        self.decrease_key_test(heap=FibonacciHeap())

    def test_heap_merge(self):
        self.merge_test(heap=FibonacciHeap())


if __name__ == "__main__":
    unittest.main()
