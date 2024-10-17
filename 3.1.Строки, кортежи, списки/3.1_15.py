n = input().split()
deliteli = []
for x in n:
    for i in range(1, int(x) + 1):
        if int(x) % i == 0:
            deliteli.append(i)
b = reversed(deliteli)
for x in b:
    if deliteli.count(x) == len(n):
        print(x)
        break
