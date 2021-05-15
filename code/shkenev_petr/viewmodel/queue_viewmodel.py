from ..model.queue import Queue


class QueueViewmodel:

    def __init__(self):
        self.queue = Queue()
        self.peek = ''
        self.make_string()

    def make_string(self):
        self.string = '\n'.join(self.queue.items)

    def enqueue(self, x):
        self.queue.enqueue(x)
        self.make_string()
        self.peek = self.queue.peek()

    def dequeue(self):
        self.queue.dequeue()
        self.make_string()
        if self.queue.is_empty():
            self.peek = ''
        else:
            self.peek = self.queue.peek()
