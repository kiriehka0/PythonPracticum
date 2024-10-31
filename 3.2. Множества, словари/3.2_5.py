n = int(input())
m = int(input())
k = []
for x in range(n + m):
    k.append(input())
if n == m:
    if len(set(k)) == n:
        print('Таких нет')
    else:
        print(len(set(k)) - ((n + m) - len(set(k))))
else:
    print(len(set(k)) - ((n + m) - len(set(k))))
