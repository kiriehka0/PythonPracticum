def sum(x):
    summa = 0
    for i in str(x):
        summa += int(i)
    return summa


n = int(input())
cnt = 0
k = 0
while cnt != n:
    a = int(input())
    k += sum(a)
    cnt += 1
print(k)
