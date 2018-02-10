s = input()
s1 = s[::-1]
a = s.find('f')
b = len(s) - s1.find('f') - 1
if a == b:
    print(a)
elif a != b and a != -1:
    print(a, b)
