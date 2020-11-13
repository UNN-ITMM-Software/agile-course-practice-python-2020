import unittest

from priority_queue.model.priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def test_is_empty_on_creation(self):
        pq = PriorityQueue()
        self.assertTrue(pq.is_empty())

    def test_becomes_empty_after_last_pop(self):
        pq = PriorityQueue()
        pq.push(1)
        pq.pop()
        self.assertTrue(pq.is_empty())

    def test_cannot_push_noninteger(self):
        pq = PriorityQueue()
        with self.assertRaises(TypeError):
            pq.push("notanumber")

    def test_cannot_pop_if_empty(self):
        pq = PriorityQueue()
        with self.assertRaises(RuntimeError):
            pq.pop()

    def test_getting_topmin(self):
        pq = PriorityQueue()
        for v in [5, 4, 2, 3]:
            pq.push(v)
        self.assertEqual(pq.top(), 2)

    def test_can_merge_two_queues(self):
        pq1 = PriorityQueue()
        pq2 = PriorityQueue()
        pq1.push(2)
        pq2.push(1)
        pq1.merge(pq2)
        self.assertEqual(pq1.top(), 1)

    def test_cannot_merge_with_wrong_arg(self):
        pq = PriorityQueue()
        with self.assertRaises(TypeError):
            pq.merge("notaPQ")

    def test_consistent_min_after_pop(self):
        pq = PriorityQueue()
        for v in [3, 2, 1]:
            pq.push(v)
        pq.pop()
        self.assertEqual(pq.top(), 2)
