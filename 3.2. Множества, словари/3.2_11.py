k = int(input())
cnt = 0
a1 = [input() for x in range(k)]
for x in set(a1):
    if a1.count(x) > 1:
        cnt += a1.count(x)
print(cnt)
