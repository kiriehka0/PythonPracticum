with open(input(), mode='r', encoding='utf-8') as f:
    a = [x.rstrip("\n") for x in f]
    b = [x.split() for x in a]
    c = set([y for x in b for y in x])
with open(input(), mode='r', encoding='utf-8') as f1:
    a1 = [x.rstrip("\n") for x in f1]
    b1 = [x.split() for x in a1]
    c1 = set([y for x in b1 for y in x])
with open(input(), mode='w', encoding='utf-8') as f2:
    k = []
    for x in c:
        if x not in c1:
            k.append(x)
    for x in c1:
        if x not in c:
            k.append(x)
    for x in sorted(k):
        f2.write(x)
        f2.write("\n")
