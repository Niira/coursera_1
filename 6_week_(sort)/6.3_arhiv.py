S, N = map(int, input().split(' '))
a = []
out = 0
while N != 0:
    n = int(input())
    a.append(n)
    N -= 1
a.sort()
for i in a:
    if S - i >= 0:
        S -= i
        out += 1
print(out)
