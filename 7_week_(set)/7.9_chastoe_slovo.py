inFile = open('input.txt', 'r', encoding='utf8')
line = inFile.read()
word = line.split()
out = {}
for i in word:
    if i in out:
        out[i] += 1
    else:
        out[i] = 1
n = 0
for j in sorted(out):
    if out[j] > n:
        n = out[j]
        result = j
print(result)
