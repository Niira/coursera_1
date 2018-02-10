P = int(input())   # процентов
X = int(input())   # рублей
Y = int(input())   # копеек
cena = (X * 100 + Y) * (100 + P) / 100
print(int(cena//100), int(cena % 100))
