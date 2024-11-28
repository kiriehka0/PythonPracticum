from sys import stdin
a = [x.split() for x in stdin]
summ = []
for i in a:
    for x in i:
        summ.append(int(x.rstrip("\n")))
print(sum(summ))
