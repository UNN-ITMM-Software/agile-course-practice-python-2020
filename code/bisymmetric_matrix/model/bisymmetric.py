import random


class BisymmetricMatrix:

    def __init__(self):
        self.mtrx = []

    def __getitem__(self, item):
        return self.mtrx[item]

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

    def is_persymmetric(self) -> bool:

        if len(self.mtrx) == 0:
            return True

        if not self.is_square():
            return False

        size = len(self.mtrx)
        index_max = size

        for i in range(size):
            for j in range(index_max):
                if self.mtrx[i][j] != self.mtrx[size-1-j][size-1-i]:
                    return False
            index_max -= 1
        return True

    def necessary_condition_for_bisymmetric(self) -> bool:

        if len(self.mtrx) == 0:
            return True

        if not self.is_square():
            return False

        diff_numbs = set()
        size = len(self.mtrx)

        for i in range(size):
            for j in range(size):
                diff_numbs.add(self.mtrx[i][j])
        if len(diff_numbs) > (((size + 1) / 2) ** 2) // 1:
            return False
        return True

    def is_bisymmetric(self) -> bool:

        if self.necessary_condition_for_bisymmetric():
            return self.is_symmetric() and self.is_persymmetric()
        return False

    def generate_random_bisymmetric_matrix(self, size: int):
        index_cor = 0

        for i in range(size):
            self.mtrx.append([])
            for j in range(0, index_cor):
                if (i + j) < size:
                    self.mtrx[i].insert(j, self.mtrx[j][i])
            for j in range(index_cor, size - index_cor):
                self.mtrx[i].insert(j, random.randrange(0, 9))
            for j in range(size - index_cor, size):
                self.mtrx[i].insert(j, self.mtrx[size-1-j][size-1-i])
            index_cor += 1

    @staticmethod
    def is_correct_vector_size(size):

        if not isinstance(size, int):
            raise TypeError

        if size == 0:
            return 0

        k = 1
        while k ** 2 <= size:
            if size == k * k:
                return 2 * k - 1
            if size == k * (k + 1):
                return 2 * k
            k += 1

        return -1

    def generate_bisymmetric_matrix_by_vector(self, vector: list):

        size = self.is_correct_vector_size(len(vector))

        if size == -1:
            raise ValueError
        elif size == 0:
            return

        index_cor = 0

        for i in range(size):
            self.mtrx.append([])
            for j in range(0, index_cor):
                if (i + j) < size:
                    self.mtrx[i].insert(j, self.mtrx[j][i])
            for j in range(index_cor, size - index_cor):
                self.mtrx[i].insert(j, vector.pop(0))
            for j in range(size - index_cor, size):
                self.mtrx[i].insert(j, self.mtrx[size-1-j][size-1-i])
            index_cor += 1
