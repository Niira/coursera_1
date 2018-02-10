def posled():
    n = int(input())
    if n != 0:
        posled()
    print(n)


posled()
