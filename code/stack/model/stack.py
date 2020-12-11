class Stack:
    def __init__(self, size=None):
        self.stack = []
        self.max_size = 100
        if size is not None:
            if not isinstance(size, int):
                raise TypeError
            elif size < 1:
                raise Exception('Incorrect max size value')
            else:
                self.max_size = size

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.max_size

    def push(self, items):
        if hasattr(items, '__iter__'):
            for item in items:
                if self.isFull():
                    raise Exception('Stack is full')
                else:
                    self.stack.append(item)
        else:
            if self.isFull():
                raise Exception('Stack is full')
            else:
                self.stack.append(items)

    def top(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        else:
            return self.stack[-1]

    def pop(self):
        top = self.top()
        del self.stack[-1]
        return top

    def get_stack(self):
        return self.stack

    def get_stack_size(self):
        return len(self.stack)

    def get_stack_max_size(self):
        return self.max_size

    def set_size(self, size):
        if not isinstance(size, int):
            raise TypeError
        elif size < 1:
            raise Exception('Incorrect max size value')
        elif size < self.get_stack_size():
            raise Exception('Small size value')
        else:
            self.max_size = size
