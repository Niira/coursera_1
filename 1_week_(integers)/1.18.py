N = int(input())
oneDay = N % 86400
hour = oneDay // 3600
minut = (oneDay % 3600) // 60
sec = (oneDay % 3600) % 60
print(hour, ':', minut // 10, minut % 10, ':', sec // 10, sec % 10, sep='')
