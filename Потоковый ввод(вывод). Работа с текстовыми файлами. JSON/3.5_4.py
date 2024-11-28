from sys import stdin
a = [x for x in stdin]
for x in a[0:-1]:
    if a[-1].rstrip("\n").upper() in x.upper():
        print(x.rstrip("\n"))
