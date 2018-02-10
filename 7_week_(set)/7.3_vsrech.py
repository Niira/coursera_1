myList = list(map(int, input().split()))
mySet = set()
for i in myList:
    if i not in mySet:
        print('NO')
        mySet.add(i)
    else:
        print('YES')
