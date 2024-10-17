h = int(input())
n = int(input())
s = []
for x in range(n):
    k = input()
    if len(k) > h:
        s.append(f'{k[:(h - 3)]}' + '...')
    else:
        s.append(k)
for x in s:
    print(x)
