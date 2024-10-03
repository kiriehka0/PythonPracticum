n = int(input())
k = int(input())
c = len(str(k * n))
cnt = 1
for x in range(n):
    cnt = x + 1
    for y in range(k):
        print(f'{cnt:>{c}}', end=' ')
        cnt += n
    print()
