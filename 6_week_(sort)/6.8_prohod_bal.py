inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
K = int(inFile.readline())   # выделяем кол-во мест
famList = inFile.readlines()   # создаем список фамилий (без кол-ва)
myList = []
for line in famList:
    bList = line.split()
    if int(bList[-1]) >= 40 and int(bList[-2]) >= 40 and int(bList[-3]) >= 40:
        allBal = int(bList[-1]) + int(bList[-2]) + int(bList[-3])
        myList.append([*bList[:-3], allBal])
myList.sort(key=lambda ind: int(ind[-1]), reverse=True)
i = 0
n = 0
for line in myList:
    bal = int(line[-1])
    i += 1
    if bal == myList[0][-1]:
        n += 1
if n == K:
    out = myList[0][-1]
if n > K:   # если кол-во людей с макс балом > кол-ва мест
    out = 1
if 0 < i <= K:
    out = 0
if i == 0:
    out = ''
if i > K:
    temp = int(myList[K][-1])
    for j in range(K, 0, -1):
        if int(myList[j][-1]) != temp:
            out = int(myList[j][-1])
            break
print(out, file=outFile)
inFile.close()
outFile.close()
