a = list(map(int, input().split()))
n = max(a)
m = min(a)
i = a.index(n)
j = a.index(m)
a[i] = m
a[j] = n
print(*a)
