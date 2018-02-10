intList = list(map(int, input().split()))
min = 1000
for i in range(len(intList)):
    if intList[i] > 0:
        if intList[i] < min:
            min = intList[i]
print(min)
