import unittest

from .queue_viewmodel import QueueViewmodel
from .logger import Logger


class TestQueueViewmodelLogging(unittest.TestCase):

    def test_new_queue_viewmodel_empty(self):
        new_queue_viewmodel = QueueViewmodel(Logger())
        assert new_queue_viewmodel.logger.messages == []

    def test_queue_viewmodel_enqueue(self):
        queue_viewmodel = QueueViewmodel(Logger())
        queue_viewmodel.enqueue('x')
        assert queue_viewmodel.logger.messages == ['Enqueued: x']

    def test_queue_viewmodel_dequeue(self):
        queue_viewmodel = QueueViewmodel(Logger())
        queue_viewmodel.enqueue('x')
        queue_viewmodel.dequeue()
        assert queue_viewmodel.logger.messages == ['Enqueued: x', 'Dequeued: x']

    def test_queue_viewmodel_dequeue_several_elements(self):
        queue_viewmodel = QueueViewmodel(Logger())
        queue_viewmodel.enqueue('x')
        queue_viewmodel.enqueue('y')
        queue_viewmodel.dequeue()
        assert queue_viewmodel.logger.messages == ['Enqueued: x', 'Enqueued: y', 'Dequeued: x']

    def test_queue_viewmodel_type(self):
        queue_viewmodel = QueueViewmodel(Logger())
        queue_viewmodel.enqueue(1)
        queue_viewmodel.dequeue()
        assert queue_viewmodel.logger.messages == ['Enqueued: 1', 'Dequeued: 1']

    def test_queue_viewmodel_get_messages_list(self):
        queue_viewmodel = QueueViewmodel(Logger())
        queue_viewmodel.enqueue('x')
        assert queue_viewmodel.logger.get_messages_list() == ['Enqueued: x']
