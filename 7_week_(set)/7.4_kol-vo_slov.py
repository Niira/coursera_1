inFile = open('input.txt', 'r', encoding='utf8')
mySet = set()
for line in inFile:
    aList = line.split()
    for i in aList:
        mySet.add(i)
print(len(mySet))
