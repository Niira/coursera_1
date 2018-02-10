from math import fabs
N = int(input())
intList = list(map(int, input().split()))
x = int(input())
if intList.count(x) != 0:
    print(x)
else:
    diff = 2000
    x1 = intList[0]
    for i in intList:
        if fabs(x - i) < diff:
            diff = fabs(x - i)
            x1 = i
    print(x1)
