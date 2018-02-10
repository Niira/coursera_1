def distance(x1, y1, x2, y2):
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return d


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
a = distance(x1, y1, x2, y2)
b = distance(x1, y1, x3, y3)
c = distance(x3, y3, x2, y2)
print('{0:.6f}'.format(a + b + c))
