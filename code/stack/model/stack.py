class Stack:
    max_size = 100

    def __init__(self, size=None):
        self.stack = []
        if size is not None:
            if type(size) is not int:
                raise TypeError
            elif size < 1:
                raise Exception('Incorrect max size value')
            else:
                self.max_size = size

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def push(self, items):
        if hasattr(items, '__iter__'):
            for item in items:
                if self.is_full():
                    raise Exception('Stack is full')
                else:
                    self.stack.append(item)
        else:
            if self.is_full():
                raise Exception('Stack is full')
            else:
                self.stack.append(items)

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            return self.stack[-1]

    def pop(self):
        top = self.top()
        del self.stack[-1]
        return top
