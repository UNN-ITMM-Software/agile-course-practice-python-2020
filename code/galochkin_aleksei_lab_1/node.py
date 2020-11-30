class Node:

    def __init__(self, k):
        self.key = k
        self.height = 1
        self.left = self.right = None

    @staticmethod
    def height(p):
        return p.height if p else 0

    @staticmethod
    def bfactor(p):
        return Node.height(p.right) - Node.height(p.left)

    @staticmethod
    def fixheight(p):
        hl = Node.height(p.left)
        hr = Node.height(p.right)
        p.height = (hl if hl > hr else hr) + 1

    @staticmethod
    def rotateright(p):
        q = p.left
        p.left = q.right
        q.right = p
        Node.fixheight(p)
        Node.fixheight(q)
        return q

    @staticmethod
    def rotateleft(q):
        p = q.right
        q.right = p.left
        p.left = q
        Node.fixheight(q)
        Node.fixheight(p)
        return p

    @staticmethod
    def balance(p):
        Node.fixheight(p)
        if Node.bfactor(p) == 2:
            if Node.bfactor(p.right) < 0:
                p.right = Node.rotateright(p.right)
            return Node.rotateleft(p)
        if Node.bfactor(p) == -2:
            if Node.bfactor(p.left) > 0:
                p.left = Node.rotateleft(p.left)
            return Node.rotateright(p)
        return p

    @staticmethod
    def insert(p, k):
        if not p:
            return Node(k)
        if k < p.key:
            p.left = Node.insert(p.left, k)
        else:
            p.right = Node.insert(p.right, k)
        return Node.balance(p)

    @staticmethod
    def findmin(p):
        return Node.findmin(p.left) if p.left else p

    @staticmethod
    def removemin(p):
        if not p.left:
            return p.right
        p.left = Node.removemin(p.left)
        return Node.balance(p)

    @staticmethod
    def remove(p, k):
        if not p:
            return 0
        if k < p.key:
            p.left = Node.remove(p.left, k)
        elif k > p.key:
            p.right = Node.remove(p.right, k)
        else:
            q = p.left
            r = p.right
            # del(p)
            if not r:
                return q
            m = Node.findmin(r)
            m.right = Node.removemin(r)
            m.left = q
            return Node.balance(m)
        return Node.balance(p)

    @staticmethod
    def containskey(p, k):
        if not p:
            return False
        if k == p.key:
            return True
        if p.left and k < p.key:
            return Node.containskey(p.left, k)
        if p.right and k > p.key:
            return Node.containskey(p.right, k)
        return False
