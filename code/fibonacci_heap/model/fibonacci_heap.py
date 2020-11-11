import math

from typing import Union, Any, List
from abc import abstractmethod


class HeapNode:
    """
    Abstract class for heap nodes
    """
    key = None
    right = None
    child = None
    val = None


class Heap:
    """
    Abstract class of the heap
    """
    @abstractmethod
    def find_min(self):
        """
        Amortized time complexity: O(1)

        """

    @abstractmethod
    def insert(self, key: Union[int, float], value: Any = None):
        """
        Insert new item as a node to the heap
        Amortized time complexity: O(1)

        :param key: Can be called with key (key)
        :param value: can be called by (key, value)
        """

    @abstractmethod
    def delete(self, node: 'HeapNode'):
        """
        Delete the given node.
        Amortized time complexity: O(log n)

        :param node: node to delete
        """

    @abstractmethod
    def delete_min(self):
        """
        Delete and returns the minimum node.
        Amortized time complexity: O(log n)
        """

    @abstractmethod
    def decrease_key(self, node: 'HeapNode', new_key: Union[int, float]):
        """
        Decrease the value of the key of the given nodes
        Amortized time complexity: O(1)

        :param node: the heap node
        :param new_key: re-define a new-key of node
        :return: the updated node
        """

    @abstractmethod
    def merge(self, heap: 'Heap'):
        """
        Merge another heap into this heap
        Amortized time complexity: O(1)

        :param heap: heap to merge
        """


class _Node(HeapNode):
    def __init__(self, key: Union[int, float], val: Any):
        self.key = key
        self.val = val
        self.parent = self.child = None
        self.left = self.right = self
        self.degree = 0
        self.flag = False


def _swap_vars(var1, var2):
    """
    Swap variables

    :param var1: first variable to swap
    :param var2: second variable to swap
    :return: swapped vars
    """
    return var2, var1


def _remove_node(node: '_Node'):
    """
    Remove element from the double linked list

    :param node: the heap node
    """
    node.left.right = node.right
    node.right.left = node.left
    node.left = node
    node.right = node
    node.parent = None


def _layer_as_list(node: '_Node') -> List['_Node']:
    """
    One node from the layer must be given

    :param node: the heap node
    :return: the whole layer of nodes as a list
    """
    items = []
    n = stop = node
    first_loop = True
    while first_loop or n != stop:
        first_loop = False
        items.append(n)
        n = n.right
    return items


class FibonacciHeap(Heap):
    """
    Implementation of FibonacciHeap
    Source info: https://en.wikipedia.org/wiki/Fibonacci_heap
    """
    def __init__(self):
        self.min = None
        self.no_nodes = 0

    def find_min(self) -> '_Node':
        """
        Amortized time complexity: O(1)

        :return: the minimum node
        """
        return self.min

    def insert(self, key: Union[int, float], value: Any = None) -> '_Node':
        """
        Insert new item as a node to the heap
        Amortized time complexity: O(1)

        :param key: key of the node. Can be called with key
        :param value: value of the key, to call with value and key (key, value)
        :return: the node
        """
        if value is None:
            value = key
        n = _Node(key, value)

        # totally new heap
        if self.no_nodes == 0:
            self.min = n
        # otherwise add to root next to min
        else:
            self._add_root(n)

        self.no_nodes += 1
        return n

    def delete(self, node: '_Node') -> None:
        """
        Delete of the given node
        Amortized time complexity: O(log n)

        :return: heap node
        """
        assert self.min is not None
        self.decrease_key(node, self.min.key - 1)
        self.delete_min()

    def delete_min(self) -> '_Node':
        """
        Delete and returns the minimum node
        Amortized time complexity: O(log n)
        :return: previous min node
        """
        prev_min = self.min
        if prev_min is not None:
            # move children to root
            if prev_min.child is not None:
                n = stop = prev_min.child
                first_loop = True
                while first_loop or n != stop:
                    first_loop = False
                    next_node = n.right
                    self._add_node_left(n, self.min)
                    n.parent = None
                    n = next_node

            # remove current min
            if self.min.right != self.min:
                self.min = prev_min.right
                _remove_node(prev_min)
                self._consolidate()
            # no nodes left
            else:
                self.min = None
                _remove_node(prev_min)

            self.no_nodes -= 1
        return prev_min

    def _consolidate(self) -> None:
        """
        Make the degrees of root elements unique, fibonacci sequence
        """
        degree_arr = [None for _ in range(int(math.log(self.no_nodes, 2)) + 2)]
        root_items = _layer_as_list(self.min)
        for n in root_items:

            degree = n.degree
            # combine nodes until no same root degrees exists
            while degree_arr[degree] is not None:
                m = degree_arr[degree]
                # make sure that n is always smaller
                if m.key < n.key:
                    n, m = _swap_vars(n, m)
                _remove_node(m)
                self._add_child(m, n)
                degree_arr[degree] = None
                degree += 1

            degree_arr[degree] = n

        self._update_root_min()

    def _update_root_min(self) -> None:
        """
        Update self.min to lowest value from the root
        """
        top = self._find_root_item()
        root_layer = _layer_as_list(top)
        self.min = min(root_layer, key=lambda n: n.key)

    def _find_root_item(self) -> '_Node':
        """
        Return an item from root layer
        """
        top_item = self.min
        while top_item.parent is not None:
            top_item = top_item.parent
        return top_item

    def decrease_key(self, node: '_Node', new_key: Union[int, float]) -> '_Node':
        """
        Decrease the value of the key of the given nodes
        Amortized time complexity: O(1)

        :param node: the heap node
        :param new_key: new key of the node, must lower than current key value.
        :return: the updated node.
        """
        assert (
                node.key > new_key
        ), 'The new_key must be lower than current when decreasing key.'

        node.key = new_key
        parent = node.parent

        # root element, simple case
        if parent is None:
            if node.key < self.min.key:
                self.min = node
        # otherwise
        elif node.key < parent.key:
            self._cut(node)
            self._cascading_cut(parent)

        return node

    def _cut(self, node: '_Node') -> None:
        """
        Move the node root level
        :param node: heap node
        """
        parent = node.parent
        parent.degree -= 1

        # if parent has only 1 child
        if parent.child == node and node.right == node:
            parent.child = None
            _remove_node(node)
        else:
            parent.child = node.right
            _remove_node(node)

        # add to the root level
        node.flag = False
        self._add_node_left(node, self.min)
        if node.key < self.min.key:
            self.min = node

    def _cascading_cut(self, node: '_Node') -> None:
        """
        Reorganize the heap to keep it in optimal form

        :param node: the heap node
        :return: parented node
        """
        parent = node.parent
        if parent is not None:
            if parent.flag:
                self._cut(node)
                self._cascading_cut(parent)
            else:
                parent.flag = True

    def merge(self, heap: 'FibonacciHeap') -> None:
        """
        Merge another heap into this heap.
        Amortized time complexity: O(1)

        :param heap: the heap node
        :return: merged node
        """
        assert isinstance(heap, FibonacciHeap)

        # move given heap between min and min.right
        # self.first <-> heap.first <-> ... <-> heap.last   <-> self.last
        # first      <-> second     <-> ... <-> second_last <-> last
        first = self.min
        last = self.min.right
        second = heap.min
        second_last = heap.min.left

        first.right = second
        second.left = first
        last.left = second_last
        second_last.right = last

        self.no_nodes += heap.no_nodes
        if heap.min.key < self.min.key:
            self.min = heap.min

    def _add_node_left(self, node: '_Node', right_node: '_Node') -> None:
        """
        Add node to left side of the given right_node

        :param node: the heap node
        :param right_node: right defined node
        :return: added node
        """
        node.right = right_node
        node.left = right_node.left
        right_node.left.right = node
        right_node.left = node

    def _add_root(self, node: '_Node') -> None:
        """
        Add node to left side of the given right_node

        :param node: the heap node
        :return: root node
        """
        self._add_node_left(node, self.min)
        if node.key < self.min.key:
            self.min = node

    def _add_child(self, child: '_Node', parent: '_Node') -> None:
        """
        Add node as child to another node
        :param child: child node
        :param parent: parent node
        :return: child node
        """
        if parent.child is None:
            parent.child = child
            child.parent = parent
        else:
            self._add_node_left(child, parent.child)
            child.parent = parent
        parent.degree += 1
