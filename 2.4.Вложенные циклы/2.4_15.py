n = int(input())
k = int(input())
c = len(str(k * n))
for x in range(n):
    for y in range(k):
        if y % 2 == 0:
            num = (y * n) + x + 1
        else:
            num = ((y + 1) * n) - x
        print(f'{num:>{c}}', end=' ')
    print()
