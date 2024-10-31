n = int(input())
a = []
for x in range(n):
    igruhki = input()
    for x in range(len(igruhki) - 2):
        if igruhki[x] == ':':
            a.append(igruhki[(x + 2):].split())
for x in a:
    for y in range(len(x)):
        for z in range(len(x[y])):
            if x[y][z] == ',':
                x[y] = x[y][:z]
b = []
b1 = []
b2 = []
for x in a:
    b.append(set(x))
for x in b:
    for x1 in x:
        b1.append(x1)
for x in b1:
    if b1.count(x) == 1:
        b2.append(x)
for x in sorted(b2):
    print(x)
