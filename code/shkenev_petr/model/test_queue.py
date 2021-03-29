import unittest

from .queue import Queue


class TestQueue(unittest.TestCase):

    def test_new_queue_is_empty(self):
        new_queue = Queue()
        assert new_queue.is_empty()

    def test_queue_is_not_empty(self):
        queue = Queue()
        queue.enqueue(1)
        assert not queue.is_empty()

    def test_size_empty_queue(self):
        queue = Queue()
        assert queue.size() == 0

    def test_size_increment(self):
        queue = Queue()
        queue.enqueue(1)
        assert queue.size() == 1

    def test_size_decrement(self):
        queue = Queue()
        queue.enqueue(1)
        queue.dequeue()
        assert queue.size() == 0

    def test_peek(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.peek() == 1

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
