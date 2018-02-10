s = input()
n = s.find(' ')
s1 = s[n+1:] + ' ' + s[:n]
print(s1)
