N = int(input())
myList = []
i = 0
while i != N:
    myList.append(input().split())
    i += 1
myList.sort(key=lambda ind: int(ind[-1]), reverse=True)
for line in myList:
    print(line[0])
