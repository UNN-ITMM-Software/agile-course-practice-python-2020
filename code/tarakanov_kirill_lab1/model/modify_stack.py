class ModifyStack:
    """
    Class ModifyStack implements
    The following operations are supported:
    * Insertion O(1)
    * Deletion top element O(1)
    * Read top element O(1)
    * Find min element in stack O(1)
    :attribute _stack: stores elements in stack
    :attribute _min_stack: stores min_elements for each stack state
    """
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def is_empty(self):
        return len(self._stack) == 0

    def size(self):
        return len(self._stack)

    def look_top(self):
        return self._stack[-1]

    def _push_empty(self, elem):
        self._stack.append(elem)
        self._min_stack.append(elem)

    def _push_one(self, elem):
        top_elem = self.look_top()
        self._stack.append(elem)
        if elem < top_elem:
            self._min_stack.append(elem)
        else:
            self._min_stack.append(top_elem)

    def push(self, val):
        if isinstance(val, list):
            self._push_empty(val[0]) if self.is_empty() else self._push_one(val[0])
            for i in val[1:]:
                self._push_one(i)
        else:
            self._push_empty(val) if self.is_empty() else self._push_one(val)

    def pop(self):
        self._stack.pop()
        self._min_stack.pop()

    def find_min(self):
        return self._min_stack[-1]
