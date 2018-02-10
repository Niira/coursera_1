pered_n = int(input())
c = 1
b = 0
while pered_n != 0:
    n = int(input())
    pered_n, n = n, pered_n
    if n == pered_n:
        c += 1
    if c > b:
        b = c
    if pered_n != n:
        c = 1
print(b)
