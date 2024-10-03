cnt = int(input())
res = 0
for i in range(cnt):
    num = int(input())
    maxi = -1
    while num > 0:
        if num % 10 > maxi:
            maxi = num % 10
        num //= 10
    res = res * 10 + maxi
print(res)
