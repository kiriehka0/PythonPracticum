from sys import stdin
stroki = [x.strip("\n") for x in stdin]
spli_t = [x.split() for x in stroki]
slova = [y for x in spli_t for y in x]
palindrom = [x for x in slova if x.upper() == x[::-1].upper()]
for x in sorted(set(palindrom)):
    print(x)
