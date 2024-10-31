k = input()
sl = dict()
while k != "":
    s = k.split()
    for x in set(s):
        if x in sl:
            sl[x] += s.count(x)
        else:
            sl[x] = 0
            sl[x] += s.count(x)
    k = input()
for x in sl:
    print(x, sl[x])
