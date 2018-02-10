def min4(a, b, c, d):
    i1 = min(a, b)
    i2 = min(i1, c)
    i3 = min(i2, d)
    return i3


A = int(input())
B = int(input())
C = int(input())
D = int(input())
print(min4(A, B, C, D))
