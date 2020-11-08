class DHeap:
    def __init__(self, d=2, data=None):
        self._d = d
        if data is None:
            self._heap = []
        else:
            if not isinstance(data, list):
                raise TypeError("Must be list")
            for elem in data:
                if not (isinstance(elem, int) or isinstance(elem, float)):
                    raise TypeError("Elements must have numeric type")
            self._heap = data
            for i in range(len(self._heap)-1, -1, -1):
                self._diving(i)

    @property
    def d(self):
        return self._d

    @property
    def heap(self):
        return self._heap.copy()

    def _parent(self, i):
        if i > 0 and i < len(self._heap):
            return (i - 1) // self._d
        else:
            return -1

    def _left_child(self, i):
        if i >= 0 and self._d * i + 1 < len(self._heap):
            return self._d * i + 1
        else:
            return -1

    def _min_child(self, i):
        lc = self._left_child(i)
        if lc == -1:
            return -1
        mc = lc
        for j in range(lc+1, min(lc + self._d, len(self._heap))):
            if self._heap[j] < self._heap[mc]:
                mc = j
        return mc

    def _emersion(self, i):
        j1 = i
        j2 = self._parent(j1)
        while j2 != -1 and self._heap[j2] > self._heap[j1]:
            self._heap[j1], self._heap[j2] = self._heap[j2], self._heap[j1]
            j1 = j2
            j2 = self._parent(j1)

    def _diving(self, i):
        j1 = i
        j2 = self._min_child(j1)
        while j2 != -1 and self._heap[j1] > self._heap[j2]:
            self._heap[j1], self._heap[j2] = self._heap[j2], self._heap[j1]
            j1 = j2
            j2 = self._min_child(j1)

    def insert(self, w):
        if not (isinstance(w, int) or isinstance(w, float)):
            raise TypeError("Elements must have numeric type")
        self._heap.append(w)
        self._emersion(len(self._heap) - 1)

    def min(self):
        return self._heap[0]

    def delete_min(self):
        if len(self._heap) == 0:
            raise RuntimeError("Can't delete minimum from empty heap")
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self._diving(0)

    def decrease_weight(self, i, delta):
        if delta < 0:
            raise ValueError("Can't increase weight")
        if i < 0 or i >= len(self._heap):
            raise ValueError("Index is out of range")
        self._heap[i] -= delta
        self._emersion(i)

    def delete(self, i):
        self.decrease_weight(i, float('Inf'))
        self.delete_min()
