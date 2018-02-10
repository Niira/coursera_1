a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4*a*c
if D > 0:
    x1 = (-D**0.5-b) / (2*a)
    x2 = (D**0.5-b) / (2*a)
    if x2 < x1:
        (x2, x1) = (x1, x2)
    print('{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
if D == 0:
    print('{0:.6f}'.format(-b/(2*a)))
