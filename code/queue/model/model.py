
class Queue():
    def __init__(self):
        self.queue = list()

    def add_to_queue(self, value):
        if value not in self.queue:
            self.queue.insert(0, value)
            return True
        return False

    def remove_from_queue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")

    def size(self):
        return len(self.queue)

    def get_elements(self):
        return " ".join(map(str, self.queue))
