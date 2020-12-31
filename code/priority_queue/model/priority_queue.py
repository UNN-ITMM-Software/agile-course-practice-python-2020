class PriorityQueue():
    def __init__(self):
        self.hb = 2
        self.ha = []
        self.currSize = -1

    def push(self, e):
        if not isinstance(e, int):
            raise TypeError("Only integers are allowed")
        self.ha.append(e)
        self.currSize += 1
        hb = self.hb+1
        i = int(self.currSize)
        j = (i - 1) // hb
        while e < self.ha[j] and j >= 0:
            self.ha[i], self.ha[j] = self.ha[j], self.ha[i]
            i, j = j, (j - 1) // hb

    def top(self):
        return self.ha[0]

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
        childless = True

        print("while childless")
        while childless:
            mchildi = (idx * hb) + 1
            if mchildi > self.currSize:
                break
            childless = False
            lb = min(self.currSize, mchildi + hb)
            mv = min(ha[mchildi:mchildi+lb])
            mchildi = mchildi + ha[mchildi:mchildi+lb].index(mv)
            if ha[idx] > ha[mchildi]:
                ha[idx], ha[mchildi] = ha[mchildi], ha[idx]
                idx = mchildi
            else:
                childless = False
        return val

    def merge(self, otherpq):
        if not isinstance(otherpq, PriorityQueue):
            raise TypeError("Error on merge: unexpected arg type")
        while not otherpq.is_empty():
            self.push(otherpq.pop())

    def is_empty(self):
        return self.currSize == 0
