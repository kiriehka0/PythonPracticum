n = []
cnt = []
while (string := input()) != 'ФИНИШ':
    string = string.lower().replace(' ', '')
    for x in string:
        if x in n:
            cnt[n.index(x)] += 1
        else:
            n.append(x)
            cnt.append(1)
maxi = 0
f = []
for x in range(len(n)):
    if cnt[x] > maxi:
        maxi = cnt[x]
        f = [n[x]]
    elif cnt[x] == maxi:
        f.append(n[x])
f.sort()
if len(f) != 0:
    print(f[0])
