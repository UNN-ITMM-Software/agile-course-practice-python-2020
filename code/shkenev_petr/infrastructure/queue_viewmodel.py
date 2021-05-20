from ..model.queue import Queue


class QueueViewmodel:

    def __init__(self, _logger):
        self.queue = Queue()
        self.peek = ''
        self.logger = _logger
        self.make_string()

    def make_string(self):
        self.queue.items = [str(i) for i in self.queue.items]
        self.string = '\n'.join(self.queue.items)
        self.history = '\n'.join(self.logger.messages)

    def enqueue(self, x):
        self.queue.enqueue(x)
        self.logger.log('Enqueued: ' + str(x));
        self.make_string()
        self.peek = self.queue.peek()

    def dequeue(self):
        x = self.queue.dequeue()
        self.logger.log('Dequeued: ' + str(x));
        self.make_string()
        if self.queue.is_empty():
            self.peek = ''
        else:
            self.peek = self.queue.peek()
