n = int(input())
m = int(input())
k = [input() for x in range(n + m)]
if n == m:
    if len(set(k)) == n:
        print('Таких нет')
    else:
        a = [x for x in k if k.count(x) == 1]
        for x in sorted(a):
            print(x)
else:
    if len(set(k)) == 1:
        print(k[0])
    a = [x for x in k if k.count(x) == 1]
    for x in sorted(a):
        print(x)
