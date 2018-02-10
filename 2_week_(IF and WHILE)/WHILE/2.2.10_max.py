m = int(input())
maximum = m
n = 1
m = int(input())
while m != 0:
    if m > maximum:
        maximum = m
        n = 0
    if m == maximum:
        n += 1
    m = int(input())
print(n)
