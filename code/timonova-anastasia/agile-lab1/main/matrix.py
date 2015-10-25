import random
import copy

class Matrix(object):
    """ Matrix class with some basis func. """

    def __init__(self, rowsCount, colsCount):
        self.rows = rowsCount
        self.cols = colsCount
        self.dataLines = []

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.dataLines])
        return s + '\n'

    @classmethod
    def makeRandom(cls, rowsCount, colsCount, lowNumberLimit=0, highNumberLimit=10):
        """ Make a random matrix with elements in range (lowNumberLimit-highNumberLimit) """

        obj = Matrix(rowsCount, colsCount)
        for x in range(obj.rows):
            obj.dataLines.append([random.randrange(lowNumberLimit, highNumberLimit) for y in range(obj.cols)])
        return obj

    @classmethod
    def makeFromList(cls, inputDataList):
        """ Create a matrix from list of user-written"""

        dataLines = inputDataList[:]
        return cls.makeMatrix(dataLines)

    @classmethod
    def makeMatrix(cls, dataLines):
        """ Helper function for creating matrix """
        
        m = len(dataLines)
        n = len(dataLines[0])
        mat = Matrix(m, n)
        mat.dataLines = dataLines
        return mat

    @classmethod
    def deleteColumnAndRow(cls, matrix, delRow, delCol):
         """ Delete specified column and row from matrix """  
         
        newMatrix = copy.deepcopy(matrix)
        del newMatrix.dataLines[delRow]
        for i in range(0, newMatrix.rows-1):
            del newMatrix.dataLines[i][delCol]
        newMatrix.rows-=1
        newMatrix.cols-=1
        return newMatrix

    @classmethod
    def calculateDeterminant(cls, matrix):
        """ Calculate determinant of matrix """
        
        if matrix.rows == 1 or matrix.cols == 1:
            return  matrix.dataLines[0][0]
        elif matrix.rows == 2 or matrix.cols == 2:
            return matrix.dataLines[0][0]* matrix.dataLines[1][1] - matrix.dataLines[1][0]*matrix.dataLines[0][1]
        else:
            determinant = 0
            for i in range(0, matrix.rows):
                subMatrix = Matrix.deleteColumnAndRow(matrix, i, 0)
                subDet = Matrix.calculateDeterminant(subMatrix)
                determinant+=(-1)**(i+2)*matrix.dataLines[i][0]*subDet
        return determinant






