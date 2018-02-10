y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())
N = 'NO'
if 1 <= y1 <= 8 and 1 <= x1 <= 8 and 1 <= y2 <= 8 and 1 <= x2 <= 8:
    if x2 > x1 and (y2 + x2) % 2 == 0 and (y1 + x1) % 2 == 0:
        N = 'YES'
print(N)
