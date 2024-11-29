from sys import stdin

a = []
n = [x.rstrip().split() for x in stdin]
for u in n:
    a.extend(u)
dict = {}
for x in a:
    n1 = x[-1].upper()
    n2 = x.lower()
    if n1 not in dict:
        dict[n1] = set()
    dict[n1].add(n2)
for key in sorted(dict.keys()):
    sorted_words = sorted(dict[key])
    print(f"{key} - {', '.join(sorted_words)}")
