import unittest

from priority_queue.logger.fakelogger import FakeLogger
from priority_queue.logger.reallogger import RealLogger
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


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.pqvm = PriorityQueueViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual("Hello pqvm init", self.pqvm.logger.get_last_msg())

    def test_logging_on_push_value(self):
        self.pqvm.push(3)
        self.assertEqual("PQ push value", self.pqvm.logger.get_last_msg())

    def test_logging_on_retrieving_top_value(self):
        self.pqvm.push(2)
        self.pqvm.top()
        self.assertEqual("PQ get top value", self.pqvm.logger.get_last_msg())

    def test_logging_on_pop_value(self):
        self.pqvm.push(1)
        self.pqvm.pop()
        self.assertEqual("PQ pop value", self.pqvm.logger.get_last_msg())


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.pqvm = PriorityQueueViewModel(RealLogger())
