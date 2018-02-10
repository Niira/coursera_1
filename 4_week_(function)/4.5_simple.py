def IsPrime(n):
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return print('NO')
        else:
            i += 1
    return print('YES')


n = int(input())
IsPrime(n)
