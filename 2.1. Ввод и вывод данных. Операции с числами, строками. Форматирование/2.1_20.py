n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
start = n * m
for x in range(1, 1000):
    for y in range(1, 1000):
        if (((k1 * x) + (k2 * y)) == start) and (x + y == n):
            print(x, y)
            break