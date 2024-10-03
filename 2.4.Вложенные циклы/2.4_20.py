n = int(input())
cnt = 0
cnt1 = 0
for x in range(10, 1, -1):
    summa = 0
    n1 = n
    while n1 > 0:
        summa += (n1 % x)
        n1 //= x
    if summa >= cnt:
        cnt = summa
        cnt1 = x
print(cnt1)
