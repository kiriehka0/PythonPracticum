n = int(input())
print('А Б В')
for a in range(1, n - 1):
    for b in range(1, n - a):
        c = n - a - b
        print(a, b, c)
