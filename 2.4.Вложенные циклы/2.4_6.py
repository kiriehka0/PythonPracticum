cnt = int(input())
n = int(input())
for x in range(cnt - 1):
    num = int(input())
    while num != 0 and n != 0:
        if num >= n:
            num %= n
        else:
            n %= num
    n += num
print(n)
