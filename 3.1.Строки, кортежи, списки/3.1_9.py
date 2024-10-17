k = input()
a = []
while k != '':
    if '#' in k:
        s = k.index('#')
        if k[:s] != '':
            a.append(k[:s])
    else:
        a.append(k)
    k = input()
for x in a:
    print(x)
