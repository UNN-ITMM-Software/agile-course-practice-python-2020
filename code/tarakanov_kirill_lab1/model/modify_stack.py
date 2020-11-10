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

