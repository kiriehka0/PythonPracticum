n = input()
a = n.split()
b = []
for i in a:
    f = {}
    k = bin(int(i))[2:]
    d = len(k)
    u = str(k).count('1')
    z = str(k).count('0')
    f["digits"] = d
    f["units"] = u
    f["zeros"] = z
    b.append(f)
print("[")
h = 0
for i in b:
    print("    {")
    h = h + 1
    for j in i:
        print(f'"{j}": {i[j]},')
    if h == len(b):
        print("    }")
    else:
        print("    },")
print("]")
