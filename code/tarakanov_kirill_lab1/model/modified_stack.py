class ModifiedStack:
    """
    Class ModifiedStack implements a data structure modified stack
    Stack works works with int and float only
    The following operations are supported:
    * Insertion O(1)
    * Deletion top element O(1)
    * Read top element O(1)
    * Find min element in stack O(1)
    :attribute _stack: stores elements in stack
    :attribute _min_stack: stores min_elements for each stack state
    """

    def __init__(self, init_list=None):
        self._stack = []
        self._min_stack = []
        if init_list:
            if not isinstance(init_list, list):
                raise TypeError('must be a list')
            for elem in init_list:
                if not isinstance(elem, int) or isinstance(elem, float):
                    raise TypeError('elems in list should be int or float only')

            self.push(init_list)

    def is_empty(self):
        return len(self._stack) == 0

    def size(self):
        return len(self._stack)

    def look_top(self):
        if self.is_empty():
            return None
        else:
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

    def pop(self, count=1):
        if count <= 0 or count > self.size() or not isinstance(count, int):
            raise ValueError('count should be positive')

        for i in range(count):
            self._stack.pop()
            self._min_stack.pop()

    def find_min(self):
        if self.is_empty():
            return None
        else:
            return self._min_stack[-1]
