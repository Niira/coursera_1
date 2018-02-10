def distance(x1, y1, x2, y2):
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return d


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print('{0:.5f}'.format(distance(x1, y1, x2, y2)))
