n = int(input())
cnt = int(input())
s = n * cnt + (n - 1)
for x in range(n):
    for y in range(n):
        print(f'{((x + 1) * (y + 1)): ^{cnt}}', end='')
        if y == n - 1:
            print()
        else:
            print('|', end='')
    if x + 1 != n:
        print('-' * s)
