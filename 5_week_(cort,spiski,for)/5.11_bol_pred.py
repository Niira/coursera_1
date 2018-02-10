intList = list(map(int, input().split()))
for i in range(1, len(intList)):
    if intList[i] > intList[i-1]:
        print(intList[i], end=' ')
