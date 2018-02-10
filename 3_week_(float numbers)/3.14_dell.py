s = input()
s1 = s[::-1]
a = s.find('h')
b = len(s) - s1.find('h')
s1 = s[:a] + s[b:]
print(s1)
