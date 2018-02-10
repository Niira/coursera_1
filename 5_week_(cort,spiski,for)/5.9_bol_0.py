intList = list(map(int, input().split()))
n = 0
for i in range(len(intList)):
    if intList[i] > 0:
        n += 1
print(n)
