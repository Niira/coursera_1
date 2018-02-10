inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
aList = inFile.readlines()   # считываем все строки из файла
aList.sort()   # создаем отсортированный список
for line in aList:
    bList = line.split()
    del bList[-2]   # удаляем номер школы
    print(*bList, file=outFile)
outFile.close()
inFile.close()
