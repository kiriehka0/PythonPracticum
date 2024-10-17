n = int(input())
k = int(input())
a = []
for x in range(n):
    a.append(k)
    k = int(input())
for x in a:
    print(x**k)
