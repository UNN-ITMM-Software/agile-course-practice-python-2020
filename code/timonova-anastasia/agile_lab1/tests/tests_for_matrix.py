import unittest
from main.matrix import Matrix


class MatrixTests(unittest.TestCase):

    def testCanCalculateDeterminantForMatrix1x1(self):
        test_matrix = Matrix.make_random(1, 1)
        det = Matrix.calculate_determinant(test_matrix)
        self.assertTrue(test_matrix.data_lines[0][0] == det)

    def testIsMatrixSquare(self):
        test_matrix = Matrix.make_random(3, 3)
        self.assertTrue(test_matrix.rows == test_matrix.cols)

    def testCanCalculateDeterminantForMatrix2x2(self):
        test_matrix = Matrix.make_from_list([[1, 3], [5, 7]])
        det = Matrix.calculate_determinant(test_matrix)
        self.assertEqual(det, -8)

    def testDeleteZeroRowAndZeroColInMatrix(self):
        test_matrix = Matrix.make_from_list([[1, 3], [5, 7]])
        det = Matrix.calculate_determinant(Matrix.delete_column_and_row(test_matrix, 0, 0))
        self.assertEqual(det, 7)

    def testCanCalculateDeterminantForMatrix3x3(self):
        test_matrix = Matrix.make_from_list([[7, 2, 0], [5, 8, 7], [1, 2, 3]])
        det = Matrix.calculate_determinant(test_matrix)
        self.assertEqual(det, 54)

    def testCanCalculateDeterminantForMatrix3x3WithSecondColumnDecomposition(self):
        test_matrix = Matrix.make_from_list([[1, 0, -3], [0, 0, 2], [-1, -2, 0]])
        det = Matrix.calculate_determinant(Matrix.delete_column_and_row(test_matrix, 0, 1))
        self.assertEqual(det, 2)

    def testCanCalculateDeterminantForMatrix6x6(self):
        test_matrix = Matrix.make_from_list([[-1, 2, 3, 4, 5, 6], [7, 0, 4, -1, 0, -3], [0, 5, -6, 0, 0, 3],
                                             [1, 0, 3, 4, 5, 6], [0, 8, 0, 1, 2, 0], [-4, 0, 6, 0, 0, -5]])
        det = Matrix.calculate_determinant(test_matrix)
        self.assertEqual(det, -96)

if __name__ == "__main__":
    unittest.main(verbosity=2)

