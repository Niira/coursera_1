def CountSort(A):   # сортировка подсчетом
    intList = [0] * 101
    for now in A:
        intList[now] += 1
    A.clear()
    for grade in range(len(intList)):
        for i in range(intList[grade]):
            A.append(grade)
    return A


A = list(map(int, input().split()))
print(*CountSort(A))
