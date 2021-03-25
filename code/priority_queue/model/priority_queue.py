class PriorityQueue():
    def __init__(self):
        self.hb = 2
        self.ha = []
        self.currSize = -1

    def pop(self):
        if self.currSize < 0:
            raise RuntimeError("Attempt to pop empty PriorityQueue")
        ha = self.ha
        val = ha[0]
        ha[0], ha[self.currSize] = ha[self.currSize], ha[0]

        self.currSize -= 1
        ha.pop()
        idx = 0
        hb = self.hb

        while True:
            mchildi = (idx * hb) + 1
            if mchildi > self.currSize:
                break
            lb = min(self.currSize, mchildi + hb)
            mv = min(ha[mchildi:mchildi+lb])
            mchildi = mchildi + ha[mchildi:mchildi+lb].index(mv)
            self.ha[idx], self.ha[mchildi] = self.ha[mchildi], self.ha[idx]
            tempidx = idx
            idx = mchildi
            if(ha[idx] <= ha[mchildi]):
                idx = tempidx
                self.ha[idx], self.ha[mchildi] = self.ha[mchildi], self.ha[idx]
                break
        return val

    def push(self, e):
        if not isinstance(e, int):
            raise TypeError("Only integers are allowed")
        self.ha.append(e)
        self.currSize += 1
        hb = self.hb
        i = int(self.currSize)
        j = (i - 1) // hb
        while(self.ha[i] < self.ha[j]):
            self.ha[i], self.ha[j] = self.ha[j], self.ha[i]
            i = j
            j = (i - 1) // hb
            if(j < 0):
                break

    def top(self):
        return self.ha[0]

    def is_empty(self):
        return self.currSize < 0
