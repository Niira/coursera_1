P = int(input())   # процентов
X = int(input())   # рублей
Y = int(input())   # копеек
K = int(input())   # кол-во лет
i = 1
cena = (X * 100 + Y) * ((100 + P) / 100)
while i != K:
    cena = int(cena * ((100 + P) / 100) + 0.000001)
    i += 1
print(int(cena//100), int(cena % 100))
