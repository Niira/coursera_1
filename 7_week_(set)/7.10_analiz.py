inFile = open('input.txt', 'r', encoding='utf8')
line = inFile.read()
word = line.split()
out = {}
for i in word:
    if i in out:
        out[i] += 1
    else:
        out[i] = 1
for key in sorted(sorted(out), key=out.get, reverse=True):
    print(key)
