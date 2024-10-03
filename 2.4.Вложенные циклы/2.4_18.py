n = int(input())
cnt = 0
k = 1
maxi = 0
while cnt <= n:
    s = 0
    for position in range(k):
        cnt += 1
        if cnt <= n:
            s += len(str(cnt))
        if position < k - 1 and cnt < n:
            s += 1
    if maxi < s:
        maxi = s
    k += 1
cnt = 0
k = 1
while cnt <= n:
    w = ''
    for p in range(k):
        cnt += 1
        if cnt <= n:
            w += str(cnt)
        if p < k - 1 and cnt < n:
            w += ' '
    k += 1
    print(f'{w:^{maxi}}')
