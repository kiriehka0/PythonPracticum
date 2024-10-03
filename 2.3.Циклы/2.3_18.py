n = int(input())
d = ''
while n != 1:
    for i in range(2, int(n) + 1):
        if n % i == 0:
            n = n / i
            d += f'{i} * '
            break
print(d.strip(' * '))
