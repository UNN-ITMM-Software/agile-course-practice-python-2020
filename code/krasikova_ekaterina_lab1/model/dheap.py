class DHeap:
    def __init__(self, d=2):
        self.d = d
        self.heap = []

    def _parent(self, i):
        if i > 0 and i < len(self.heap):
            return (i - 1) // self.d
        else:
            return -1

    def _left_child(self, i):
        if i >= 0 and self.d * i + 1 < len(self.heap):
            return self.d * i + 1
        else:
            return -1

    def _min_child(self, i):
        lc = self._left_child(i)
        if lc == -1:
            return -1
        mc = lc
        for j in range(lc+1, min(lc + self.d, len(self.heap))):
            if self.heap[j] < self.heap[mc]:
                mc = j
        return mc

    def insert(self, w):
        self.heap.append(w)
        j1 = len(self.heap) - 1
        j2 = self._parent(j1)
        while j2 != -1 and self.heap[j2] > self.heap[j1]:
            self.heap[j1], self.heap[j2] = self.heap[j2], self.heap[j1]
            j1 = j2
            j2 = self._parent(j1)
    
    def min(self):
        return self.heap[0]

    def delete_min(self):
        if len(self.heap) == 0:
            raise RuntimeError("Can't delete minimum from empty heap")
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        j1 = 0
        j2 = self._min_child(j1)
        while j2 != -1 and self.heap[j1] > self.heap[j2]:
            self.heap[j1], self.heap[j2] = self.heap[j2], self.heap[j1]
            j1 = j2
            j2 = self._min_child(j1)
