N = int(input())
minDay = N % 1440   # Остаток от кол-ва минут в сутках
print((minDay // 60), (minDay % 60))
