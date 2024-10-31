a = []
a1 = []
for x in range(n := int(input())):
    k = input()
    a.append(k.split()[0])
    a1.append(k.split()[1:])
sl = dict(zip(a, a1))
k1 = input()
h = []
for x in sl:
    if k1 in sl[x]:
        h.append(x)
if len(h) == 0:
    print('Таких нет')
else:
    for x in sorted(h):
        print(x)
