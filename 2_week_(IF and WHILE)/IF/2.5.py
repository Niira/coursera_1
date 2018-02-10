x = int(input())
y = int(input())
X = int(input())
Y = int(input())
if (x - X == 1 or x - X == -1) and (y - Y == 1 or y - Y == -1):
    print('YES')
elif (x == X or y == Y) and (x-X == 1 or x-X == -1 or y-Y == 1 or y-Y == -1):
    print('YES')
else:
    print('NO')
