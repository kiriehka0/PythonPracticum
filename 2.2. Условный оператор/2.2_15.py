a = (input())
b = (input())
a1 = int(a[0])
a2 = int(a[1])
b1 = int(b[0])
b2 = int(b[1])
g = [a1, a2, b1, b2]
g.sort()
s = str(g[3]) + str((g[1] + g[2]) % 10) + str(g[0])
print(s)

