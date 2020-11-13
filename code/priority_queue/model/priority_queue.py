class PriorityQueue():
    def __init__(self):
        self.hb = 2
        self.ha = []
        self.arrlen = 0

    def push(self, e):
        if not type(e) is int:
            raise TypeError("Only integers are allowed")
        self.ha.append(e)
        self.arrlen += 1
        l = self.arrlen
        hb = self.hb
        i = int(l) - 1
        j = (i - 1) // hb
        while(e < self.ha[j] and (j >= 0)):
            self.ha[i], self.ha[j] = self.ha[j], self.ha[i]
            i, j = j, ((j - 1) // hb)

    def top(self):
        return self.ha[0]

    def pop(self):
        if(self.arrlen == 0):
            raise RuntimeError("Attempt to pop empty PriorityQueue")
        ha = self.ha
        l = self.arrlen - 1
        val = ha[0]
        ha[0], ha[l] = ha[l], ha[0]
        ha.pop()
        self.arrlen -= 1
        l = self.arrlen - 1
        idx = 0
        hb = self.hb
        childLess = True

        while(childLess):
            mChIdx = (idx * hb) + 1
            if(mChIdx >= l):
                break
            childLess = False
            i, j = mChIdx, 0
            lb = min(l, mChIdx + hb)
            mv = min(ha[mChIdx : lb])
            mChIdx = [i for i in range(mChIdx, lb) if(ha[i] == mv)][0]
            if(ha[idx] > ha[mChIdx]):
                ha[idx], ha[mChIdx] = ha[mChIdx], ha[idx]
                indx = mChIdx
                childLess = True
            else:
                childLess = False
        return val

    def merge(otherpq):
        if(not(type(otherpq) == PriorityQueue)):
            raise TypeError("Error on merge: unexpected arg type")
        while(not other.pq.is_empty()):
            self.push(otherpq.pop())

    def is_empty(self):
        return self.arrlen == 0
