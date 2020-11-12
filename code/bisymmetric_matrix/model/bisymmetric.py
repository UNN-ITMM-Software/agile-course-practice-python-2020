class BisymmetricMatrix:

    def __init__(self):
        self.mtrx = []

    def init_matrix(self, mtrx: list):
        self.mtrx = mtrx

    def is_square(self) -> bool:
        size = len(self.mtrx)

        if size == 0:
            return True

        for row in self.mtrx:
            if len(row) != size:
                return False
        return True

    def is_symmetric(self) -> bool:

        if len(self.mtrx) == 0:
            return True

        if not self.is_square():
            return False

        size = len(self.mtrx)
        index_min = 1

        for i in range(size-1):
            for j in range(index_min, size):
                if self.mtrx[i][j] != self.mtrx[j][i]:
                    return False
            index_min += 1
        return True
