n = int(input())
k = int(input())
k1 = len(str(k * n))
if n > 0 and k > 0:
    for x in range(n):
        for y in range(k):
            if (x % 2) == 0:
                num = x * k + y + 1
            else:
                num = (x + 1) * k - y
            print(f'{num:>{k1}}', end=' ')
        print()
