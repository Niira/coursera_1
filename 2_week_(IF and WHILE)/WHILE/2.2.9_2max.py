first = int(input())
n = int(input())
if n > first:
    sec, first = first, n
else:
    sec, first = n, first
n = int(input())
while n != 0:
    if n > first:
        sec, first = first, n
    elif sec < n <= first:
        sec = n
    n = int(input())
print(sec)
