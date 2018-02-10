from math import fabs
n = int(input())   # количество селений
s_to_n = list(map(int, input().split()))   # расстояние от начала дороги до селения
listSelen = []
for i in range(n):
    listSelen.append((s_to_n[i], i+1))
listSelen.sort()
m = int(input())   # количество бомбоубежищ
s_to_m = list(map(int, input().split()))   # расстояние от начала дороги до бомбоубежища
listUbeg = []
for i in range(m):
    listUbeg.append((s_to_m[i], i+1))
listUbeg.sort()
result = []
print(listSelen)
print(listUbeg)