import unittest

from .queue_viewmodel import QueueViewmodel

class TestQueueViewmodel(unittest.TestCase):

    def test_new_queue_viewmodel_empty(self):
        new_queue_viewmodel = QueueViewmodel()
        assert new_queue_viewmodel.string == ''

    def test_queue_viewmodel_enqueue(self):
        queue_viewmodel = QueueViewmodel()
        queue_viewmodel.enqueue('x')
        assert queue_viewmodel.string == 'x'

    def test_queue_viewmodel_enqueue_several_elements(self):
        queue_viewmodel = QueueViewmodel()
        queue_viewmodel.enqueue('x')
        queue_viewmodel.enqueue('y')
        assert queue_viewmodel.string == 'x\ny'

    def test_queue_viewmodel_peek_enqueue(self):
        queue_viewmodel = QueueViewmodel()
        queue_viewmodel.enqueue('x')
        queue_viewmodel.enqueue('y')
        assert queue_viewmodel.peek == 'x'

    def test_queue_viewmodel_peek_dequeue(self):
        queue_viewmodel = QueueViewmodel()
        queue_viewmodel.enqueue('x')
        queue_viewmodel.dequeue()
        assert queue_viewmodel.peek == ''

    def test_queue_viewmodel_dequeue(self):
        queue_viewmodel = QueueViewmodel()
        queue_viewmodel.enqueue('x')
        queue_viewmodel.enqueue('y')
        queue_viewmodel.dequeue()
        assert queue_viewmodel.string == 'y'

