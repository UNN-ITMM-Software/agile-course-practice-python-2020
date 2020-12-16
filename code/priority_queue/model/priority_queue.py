class PriorityQueue():
    def __init__(self):
        self.hb = 2
        self.ha = []
        self.arrlen = 0

    def push(self, e):
        if not isinstance(e, int):
            raise TypeError("Only integers are allowed")
        self.ha.append(e)
        self.arrlen += 1
        length = self.arrlen
        hb = self.hb
        i = int(length) - 1
        j = (i - 1) // hb
        while e < self.ha[j] and j >= 0:
            self.ha[i], self.ha[j] = self.ha[j], self.ha[i]
            i, j = j, ((j - 1) // hb)

    def top(self):
        return self.ha[0]

    def pop(self):
        if self.arrlen == 0:
            raise RuntimeError("Attempt to pop empty PriorityQueue")
        ha = self.ha
        length = self.arrlen - 1
        val = ha[0]
        ha[0], ha[length] = ha[length], ha[0]
        ha.pop()
        self.arrlen -= 1
        length = self.arrlen - 1
        idx = 0
        hb = self.hb
        childless = True

        while childless:
            mchildi = (idx * hb) + 1
            if mchildi >= length:
                break
            childless = False
            lb = min(length, mchildi + hb)
            mv = min(ha[mchildi:lb])
            mchildi = [i for i in range(mchildi, lb) if ha[i] == mv][0]
            if ha[idx] > ha[mchildi]:
                ha[idx], ha[mchildi] = ha[mchildi], ha[idx]
                idx = mchildi
                childless = True
            else:
                childless = False
        return val

    def merge(self, otherpq):
        if not isinstance(otherpq, PriorityQueue):
            raise TypeError("Error on merge: unexpected arg type")
        while not otherpq.is_empty():
            self.push(otherpq.pop())

    def is_empty(self):
        return self.arrlen == 0
