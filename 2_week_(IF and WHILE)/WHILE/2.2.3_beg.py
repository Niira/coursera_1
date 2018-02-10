x = float(input())
y = float(input())
delta = x/10
i = 1
while x < y:
    x = x + delta
    delta = x / 10
    i = i + 1
print(i)
