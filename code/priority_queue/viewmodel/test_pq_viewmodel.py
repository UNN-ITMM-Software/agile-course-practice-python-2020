import unittest

from priority_queue.viewmodel.pq_viewmodel import PriorityQueueViewModel


class TestPriorityQueueViewModel(unittest.TestCase):

    def setUp(self):
        self.pqvm = PriorityQueueViewModel()

    def test_is_empty_on_creation(self):
        self.assertTrue(self.pqvm.is_empty())

    def test_becomes_empty_after_last_pop(self):
        self.pqvm.push(1)
        self.pqvm.pop()
        self.assertTrue(self.pqvm.is_empty())

    def test_cannot_push_noninteger(self):
        with self.assertRaises(TypeError):
            self.pqvm.push("notanumber")

    def test_cannot_pop_if_empty(self):
        with self.assertRaises(RuntimeError):
            self.pqvm.pop()

    def test_getting_topmin(self):
        for v in [5, 4, 2, 3]:
            self.pqvm.push(v)
        self.assertEqual(self.pqvm.top(), '2')

    def test_consistent_min_after_pop(self):
        for v in [3, 2, 1]:
            self.pqvm.push(v)
        self.pqvm.pop()
        self.assertEqual(self.pqvm.top(), '2')
