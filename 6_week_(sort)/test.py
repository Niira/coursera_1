n = float(input())
if 0 <= n % 5 < 3:
    print('Зеленый')
elif 3 <= n % 5 < 4:
    print('Желтый')
elif 4 <= n % 5 < 5:
    print('Красный')
