class DHeap:
    def __init__(self, d=2):
        self.d = d
        self.heap = []

    def _parent(self, i):
        if i > 0 and i < len(self.heap):
            return (i - 1) // self.d
        else:
            return -1

    def insert(self, w):
        self.heap.append(w)
        j1 = len(self.heap) - 1
        j2 = self._parent(j1)
        while j2 != -1 and self.heap[j2] > self.heap[j1]:
            self.heap[j1], self.heap[j2] = self.heap[j2], self.heap[j1]
            j1 = j2
            j2 = self._parent(j1)