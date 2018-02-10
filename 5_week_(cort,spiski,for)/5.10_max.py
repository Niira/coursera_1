intList = list(map(int, input().split()))
max = 0
n = 0
for i in range(len(intList)):
    if intList[i] >= max:
        max = intList[i]
        n = i
print(max, n)
