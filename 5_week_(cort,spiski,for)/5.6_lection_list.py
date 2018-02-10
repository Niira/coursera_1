a = list('abcde')   # создание списка из строки
s = ''.join(a)   # собрать (объединить) список в строку
wordList = input().split()   # считывание списка (разделитель по умолчанию пробел)
intList = list(map(int, input().split()))   # map-применение функции к каждому объекту списка (считываем список чисел)
intList = [int(i) for i in input().split()]   # другой способ считать список чисел

print(' '.join(map(str, intList)))   # вывод значений из списка
print(*intList)   # другой способ вывода