inFile = open('input.txt', 'r', encoding='utf8')
word = inFile.read()
word1 = word.split()
out = {}
for elem in word1:
    if out.get(elem, -1) < 0:
        print(0, end=' ')
        out[elem] = 0
    else:
        out[elem] = out.get(elem, 0) + 1
        print(out[elem], end=' ')
