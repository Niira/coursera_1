A = int(input())
B = int(input())
C = int(input())
result = 'NO'
if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
    if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
        result = 'YES'
print(result)
