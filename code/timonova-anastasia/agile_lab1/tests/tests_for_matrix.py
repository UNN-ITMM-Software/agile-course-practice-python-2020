import unittest
from main.matrix import Matrix

class MatrixTests(unittest.TestCase):

    def testCanCalculateDeterminantForMatrix1x1(self):
        testMatrix = Matrix.makeRandom(1,1)
        det = Matrix.calculateDeterminant(testMatrix)
        self.assertTrue( testMatrix.dataLines[0][0]  == det)

    def testIsMatrixSquare(self):
        testMatrix = Matrix.makeRandom(3,3)
        self.assertTrue( testMatrix.rows == testMatrix.cols)

    def testCanCalculateDeterminantForMatrix2x2(self):
        testMatrix = Matrix.makeFromList([[1, 3], [5, 7]])
        det = Matrix.calculateDeterminant(testMatrix)
        self.assertEqual(det, -8)

    def testDeleteZeroRowAndZeroColInMatrix(self):
        testMatrix = Matrix.makeFromList([[1, 3], [5, 7]])
        det = Matrix.calculateDeterminant(Matrix.deleteColumnAndRow(testMatrix, 0, 0))
        self.assertEqual(det, 7)

    def testCanCalculateDeterminantForMatrix3x3(self):
        testMatrix = Matrix.makeFromList([[7, 2, 0], [5, 8, 7], [1, 2, 3]])
        det = Matrix.calculateDeterminant(testMatrix)
        self.assertEqual(det, 54)

    def testCanCalculateDeterminantForMatrix3x3WithSecondColumnDecomposition(self):
        testMatrix = Matrix.makeFromList([[1, 0, -3], [0, 0, 2],[-1, -2, 0]])
        det = Matrix.calculateDeterminant(Matrix.deleteColumnAndRow(testMatrix, 0, 1))
        self.assertEqual(det, 2)

    def testCanCalculateDeterminantForMatrix6x6(self):
        testMatrix = Matrix.makeFromList([[-1, 2, 3, 4, 5, 6],[7, 0, 4, -1, 0, -3],[0, 5, -6, 0, 0, 3],[1, 0, 3, 4, 5, 6], [0, 8, 0, 1, 2, 0],[-4, 0, 6, 0, 0, -5]])
        det = Matrix.calculateDeterminant(testMatrix)
        self.assertEqual(det, -96)

if __name__ == "__main__":
    unittest.main(verbosity=2)