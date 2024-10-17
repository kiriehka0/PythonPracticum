n = int(input())
k = input()
b = k.upper()
a = []
s = []
for x in range(n):
    a.append(b)
    s.append(k)
    k = input()
    b = k.upper()
for x in range(len(a)):
    if b in a[x]:
        print(s[x])
