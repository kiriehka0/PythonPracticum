n = int(input())
m = int(input())
s = []
for x in range(n):
    s.append(input())
for y in range(m):
    s.append(input())
if (n + m) == len(set(s)):
    print('Таких нет')
if len(set(s)) < (n + m):
    print((n + m) - len(set(s)))
