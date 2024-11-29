from itertools import product, repeat

n = int(input())
a = [input() for _ in range(n)]
b = [sorted(set(a[x].split(", "))) for x in range(n)]
for i in product(*b):
    print(*i, sep="")
