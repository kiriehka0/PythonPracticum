n = int(input())
cnt = 0
cnt1 = 0
k = []
while cnt != n:
    a = int(input())
    k.append(a)
    cnt += 1
for x in k:
    if str(x) == str(x)[::-1]:
        cnt1 += 1
print(cnt1)
