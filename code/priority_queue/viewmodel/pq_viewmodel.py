from priority_queue.model.priority_queue import PriorityQueue


class PriorityQueueViewModel:
    def __init__(self):
        self.pq = PriorityQueue()

    def push(self, e):
        self.pq.push(e)

    def top(self):
        return str(self.pq.top())

    def pop(self):
        self.pq.pop()

    def is_empty(self):
        return self.pq.is_empty()
