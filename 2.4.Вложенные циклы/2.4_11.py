n = int(input())
cnt = 0
for i in range(n):
    if (num := int(input())) > 1:
        s = True
        k = 2
        while k <= int(num ** 0.5) and s:
            if num % k == 0:
                s = False
            else:
                k += 1
        if s is True:
            cnt += 1
print(cnt)
