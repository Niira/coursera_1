def merge(A, B):
    C = []
    i, j = 0, 0
    for n in range(len(A) + len(B)):
        if i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        elif i < len(A):
            C.append(A[i])
            i += 1
        elif j < len(B):
            C.append(B[j])
            j += 1
    return C


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*merge(A, B))
