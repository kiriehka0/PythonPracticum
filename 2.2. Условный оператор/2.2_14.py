a = input()
a1 = a[0]
a2 = a[1]
a3 = a[2]
k = int(a1 + a2)
k1 = int(a1 + a3)
k2 = int(a2 + a3)
k3 = int(a2 + a1)
k4 = int(a3 + a1)
k5 = int(a3 + a2)
d = []
if len(str(k)) == 2:
    d.append(k)
if len(str(k1)) == 2:
    d.append(k1)
if len(str(k2)) == 2:
    d.append(k2)
if len(str(k3)) == 2:
    d.append(k3)
if len(str(k4)) == 2:
    d.append(k4)
if len(str(k5)) == 2:
    d.append(k5)
print(min(d), max(d))