n = input()
n2 = input()
with open(n, "r", encoding="utf-8") as f1:
    with open(n2, "w", encoding="utf-8") as f:
        for x in f1:
            x = x.rstrip().replace("\t", "")
            b = x.split()
            if len(b) != 0:
                print(*b, file=f)
