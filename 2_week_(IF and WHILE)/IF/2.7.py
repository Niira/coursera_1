x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if x1 % 2 == x % 2 and y % 2 == y1 % 2:
    print('YES')
elif x % 2 != x1 % 2 and y % 2 != y1 % 2:
    print('YES')
else:
    print('NO')
