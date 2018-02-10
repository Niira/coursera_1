n = int(input())
slovar = {}
slovar1 = {}
for i in range(n):
    line = input().split()
    slovar[line[0]] = line[1]
    slovar1[line[1]] = line[0]
word = input()
if word in slovar:
    print(slovar[word])
else:
    print(slovar1[word])
