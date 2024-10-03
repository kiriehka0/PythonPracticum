n = int(input())
k = int(input())
k1 = len(str(n * k))
for i in range(1, n + 1):
    for j in range(k * (i - 1) + 1, k * i + 1):
        print(f'{j:>{k1}}', end=' ')
        if j == k * i:
            print()
