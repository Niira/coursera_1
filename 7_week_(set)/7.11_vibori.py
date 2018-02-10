inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
aList = inFile.readlines()   # считываем все строки из файла
candidate = {}
cort = []
for i in aList:
    if i in candidate:
        candidate[i] += 1
    else:
        candidate[i] = 1
for j in candidate:
    cort.append((candidate[j], j))
cort.sort(reverse=True)
if int(cort[0][0]) > len(aList)/2:
    print(cort[0][1], end='', file=outFile)
else:
    print(cort[0][1], end='', file=outFile)
    print(cort[1][1], end='', file=outFile)
outFile.close()
