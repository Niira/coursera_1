from sys import stdin
from copy import deepcopy


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
        result = []
        numbers = []
        for i in range(len(self.L)):
            for j in range(len(self.L[i])):
                s1 = self.L[i][j] + other.L[i][j]
                numbers.append(s1)
                if len(numbers) == len(self.L):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

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

    def __rmul__(self, other):
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


exec(stdin.read())
