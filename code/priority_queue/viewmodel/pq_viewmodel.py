from priority_queue.model.priority_queue import PriorityQueue
from priority_queue.logger.reallogger import RealLogger


class PriorityQueueViewModel:
    def __init__(self, logger=RealLogger()):
        self.pq = PriorityQueue()
        self.logger = logger
        self.logger.log("Hello pqvm init")

    def push(self, e):
        self.logger.log("PQ push value")
        self.pq.push(e)

    def top(self):
        self.logger.log("PQ get top value")
        return str(self.pq.top())

    def pop(self):
        self.logger.log("PQ pop value")
        self.pq.pop()

    def is_empty(self):
        return self.pq.is_empty()
