import unittest

from model import Queue


class QueueTest(unittest.TestCase):
    def test_cat_create_queue(self):
        queue = Queue()
        self.assertTrue(isinstance(queue, Queue))
    
    def test_can_add_to_queue_first(self):
        queue = Queue()
        queue.addToQueue(1)
        queue.addToQueue(2)
        self.assertEqual('2 1', queue.get_elements())
      
    def test_can_add_to_queue_second(self):
        queue = Queue()
        queue.addToQueue('worker')
        queue.addToQueue('student')
        self.assertEqual('student worker', queue.get_elements())
        
    def test_can_add_to_queue_third(self):
        queue = Queue()
        queue.addToQueue('a')
        queue.addToQueue('b')
        self.assertEqual('b a', queue.get_elements())

    def test_can_remove_from_queue_first(self):
        queue = Queue()
        queue.addToQueue('one')
        queue.addToQueue('two')
        queue.addToQueue('three')
        queue.removefromQueue()
        self.assertEqual('three two', queue.get_elements())

    def test_can_remove_from_queue_second(self):
        queue = Queue()
        queue.addToQueue(123)
        queue.addToQueue(456)
        queue.addToQueue(789)
        queue.removefromQueue()
        self.assertEqual('789 456', queue.get_elements())

    def test_can_remove_from_queue_third(self):
        queue = Queue()
        queue.addToQueue('hello')
        queue.addToQueue(13)
        queue.addToQueue('wall')
        queue.removefromQueue()
        self.assertEqual('wall 13', queue.get_elements())

if __name__ == '__main__':
    unittest.main()