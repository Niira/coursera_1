n = int(input())
flag = input()
res = set(range(1, n + 1))
while flag != 'HELP':
    cur = set(map(int, flag.split()))
    ans = input()
    if ans == 'YES':
        res &= cur
    elif ans == 'NO':
        res -= cur
    flag = input()
print(*sorted(res))
