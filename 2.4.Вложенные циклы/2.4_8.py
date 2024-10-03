cnt = int(input())
s = ''
n = 0
for i in range(cnt):
    n1 = input()
    num = int(input())
    summa = 0
    while num > 0:
        summa += num % 10
        num //= 10
    if summa >= n:
        n = summa
        s = n1
print(s)
