import copy
import math


class SegmentTree(object):
    def __init__(self, tree_type):
        if tree_type not in ['max', 'min', 'sum']:
            raise TypeError('Incorrect type of segment tree. Expected: max\\min\\sum')
        self.type = tree_type

    def _build_tree(self, vertex, left, right):
        if left == right:
            self.tree[vertex] = self.array[left]
        else:
            mid = (left + right) // 2
            self._build_tree(vertex * 2, left, mid)
            self._build_tree(vertex * 2 + 1, mid + 1, right)

            left_child = self.tree[vertex * 2]
            right_child = self.tree[vertex * 2 + 1]

            if self.type == 'sum':
                self.tree[vertex] = left_child + right_child
            elif self.type == 'min':
                self.tree[vertex] = min(left_child, right_child)
            elif self.type == 'max':
                self.tree[vertex] = max(left_child, right_child)

    def build(self, array):
        if not isinstance(array, list):
            raise TypeError('Incorrect type of input array. Expected: list')

        for element in array:
            if not isinstance(element, int):
                raise TypeError('Incorrect type of input array\'s elements. Expected: int')

        self.array = copy.deepcopy(array)
        self.size = len(array)

        self.tree = [0] * self.size * 4

        self._build_tree(1, 0, self.size - 1)

    def _get(self, left, right, vertex, begin, end):
        if left <= begin and end <= right:
            return self.tree[vertex]

        if end < left or right < begin:
            if self.type == 'sum':
                return 0
            elif self.type == 'min':
                return math.inf
            elif self.type == 'max':
                return -math.inf

        mid = (begin + end) // 2

        left_child = self._get(left, right, vertex * 2, begin, mid)
        right_child = self._get(left, right, vertex * 2 + 1, mid + 1, end)

        if self.type == 'sum':
            return left_child + right_child
        elif self.type == 'min':
            return min(left_child, right_child)
        elif self.type == 'max':
            return max(left_child, right_child)

    def get(self, left, right):
        if right < left:
            raise IndexError('Wrong indices: right bound < left bound')

        if right + 1 > self.size or left < 0:
            raise IndexError('Wrong indices: indices is out of bounds')

        return self._get(left, right, 1, 0, self.size - 1)

    def _update(self, index, value, vertex, begin, end):
        if index <= begin and end <= index:
            self.array[index] = value
            self.tree[vertex] = value
            return

        if end < index or index < begin:
            return

        mid = (begin + end) // 2

        self._update(index, value, vertex * 2, begin, mid)
        self._update(index, value, vertex * 2 + 1, mid + 1, end)

        left_child = self.tree[vertex * 2]
        right_child = self.tree[vertex * 2 + 1]

        if self.type == 'sum':
            self.tree[vertex] = left_child + right_child
        elif self.type == 'min':
            self.tree[vertex] = min(left_child, right_child)
        elif self.type == 'max':
            self.tree[vertex] = max(left_child, right_child)

    def update(self, index, new_value):
        if index + 1 > self.size or index < 0:
            raise IndexError('index is out of bounds')
        self._update(index, new_value, 1, 0, self.size - 1)
