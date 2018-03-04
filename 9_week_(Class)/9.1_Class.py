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


exec(stdin.read())
