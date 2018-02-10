n = int(input())
i = 2
S = 1.0
while i <= n:
    S += 1 / i**2
    i += 1
print('{0:.5f}'.format(S))
