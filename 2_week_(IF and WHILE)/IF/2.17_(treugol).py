a = int(input())
b = int(input())
c = int(input())
typ = ''
if b > a:
    (b, a) = (a, b)
if c > a:
    (c, a) = (a, c)
if a + b > c > 0 and a + c > b > 0 and b + c > a > 0:
    if a**2 < b**2 + c**2:
        typ = 'acute'
    elif a**2 == b**2 + c**2:
        typ = 'rectangular'
    elif a**2 > b**2 + c**2:
        typ = 'obtuse'
else:
    typ = 'impossible'
print(typ)
