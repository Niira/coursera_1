s = input()
pos = 0
i = 0
n = -2
while s.find('f', pos) != -1:
    pos = s.find('f', pos) + 1
    i += 1
    if i == 1:
        n = -1
    if i == 2:
        n = pos - 1
print(n)
