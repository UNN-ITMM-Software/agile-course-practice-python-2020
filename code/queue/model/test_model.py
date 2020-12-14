import unittest

from queue.model.model import Queue


class QueueTest(unittest.TestCase):
    def test_cat_create_queue(self):
        queue = Queue()
        self.assertTrue(isinstance(queue, Queue))

    def test_can_add_to_queue_first(self):
        queue = Queue()
        queue.add_to_queue(1)
        queue.add_to_queue(2)
        self.assertEqual('2 1', queue.get_elements())

    def test_can_add_to_queue_second(self):
        queue = Queue()
        queue.add_to_queue('worker')
        queue.add_to_queue('student')
        self.assertEqual('student worker', queue.get_elements())

    def test_can_add_to_queue_third(self):
        queue = Queue()
        queue.add_to_queue('a')
        queue.add_to_queue('b')
        self.assertEqual('b a', queue.get_elements())

    def test_can_remove_from_queue_first(self):
        queue = Queue()
        queue.add_to_queue('one')
        queue.add_to_queue('two')
        queue.add_to_queue('three')
        queue.remove_from_queue()
        self.assertEqual('three two', queue.get_elements())

    def test_can_remove_from_queue_second(self):
        queue = Queue()
        queue.add_to_queue(123)
        queue.add_to_queue(456)
        queue.add_to_queue(789)
        queue.remove_from_queue()
        self.assertEqual('789 456', queue.get_elements())

    def test_can_remove_from_queue_third(self):
        queue = Queue()
        queue.add_to_queue('hello')
        queue.add_to_queue(13)
        queue.add_to_queue('wall')
        queue.remove_from_queue()
        self.assertEqual('wall 13', queue.get_elements())

    def test_can_add_empty_to_queue(self):
        queue = Queue()
        queue.add_to_queue('')
        self.assertEqual('', queue.get_elements())

    def test_can_remove_empty_from_queue(self):
        queue = Queue()
        queue.remove_from_queue()
        self.assertEqual('', queue.get_elements())

    def test_can_get_queue_size(self):
        queue = Queue()
        queue.add_to_queue('anxiety')
        queue.size()
        self.assertTrue(queue.size() > 0)
