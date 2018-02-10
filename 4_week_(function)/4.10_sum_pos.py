def summPos():
    n = int(input())
    if n != 0:
        return n + summPos()
    return 0

print(summPos())
