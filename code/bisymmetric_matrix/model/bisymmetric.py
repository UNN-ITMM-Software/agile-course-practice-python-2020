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
