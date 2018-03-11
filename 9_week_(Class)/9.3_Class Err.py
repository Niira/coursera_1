from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2


class Matrix:
    def __init__(self, L):
        self.L = deepcopy(L)

    def __str__(self):
        joined = '\n'.join(['\t'.join([
            str(i) for i in row]) for row in self.L])
        string = ''
        for row in self.L:
            for i in row:
                string += str(i)
        return joined

    def size(self):
        sizepair = (len(self.L), len(self.L[0]))
        return sizepair

    def __add__(self, other):
        if len(self.L) == len(other.L):
            lenght = len(self.L[0])
            for row in self.L:
                if len(row) != lenght:
                    raise MatrixError(self, other)
            for row2 in other.L:
                if len(row2) != lenght:
                    raise MatrixError(self, other)
            result = []
            numbers = []
            for i in range(len(self.L)):
                for j in range(len(self.L[0])):
                    summa = other.L[i][j] + self.L[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.L[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        result = []
        numbers = []
        for i in range(len(self.L)):
            for j in range(len(self.L[i])):
                s1 = self.L[i][j] * other
                numbers.append(s1)
                if len(numbers) == len(self.L):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        tmatrix = list(zip(*self.L))
        self.L = tmatrix
        return Matrix(tmatrix)

    def transposed(self):
        tmatrix = list(zip(*self.L))
        return Matrix(tmatrix)


exec(stdin.read())
