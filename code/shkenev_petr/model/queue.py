class Queue:

    def __init__(self):
        self.items = []    

    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, x):
        self.items.append(x)
    
    def peek(self):
        return self.items[0]
    
    def dequeue(self):
        return self.items.pop(0)
