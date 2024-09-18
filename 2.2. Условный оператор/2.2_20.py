a = input()
b = input()
c = input()
k = []
if "зайка" in a:
    k.append(a)
if "зайка" in b:
    k.append(b)
if "зайка" in c:
    k.append(c)
if len(k) == 1:
    print(k[0], len(k[0]))
if len(k) >= 2:
    print(min(k), len(min(k)))