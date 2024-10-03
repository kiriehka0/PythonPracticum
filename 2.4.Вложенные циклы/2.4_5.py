n = int(input())
cnt = 0
cnt1 = 0
while cnt != n:
    a = input()
    k = []
    while a != "ВСЁ":
        if a == "зайка":
            k.append(0)
        a = input()
    cnt += 1
    if len(k) >= 1:
        cnt1 += 1
print(cnt1)
