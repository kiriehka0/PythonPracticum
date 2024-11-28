from sys import stdin
a = [x for x in stdin]
b = []
for x in a:
    if '#' in x:
        if x[0] == '#':
            continue
        else:
            x = x[:x.index('#')]
            b.append(x)
    else:
        b.append(x)
for x in b:
    print(x.rstrip("\n"))
