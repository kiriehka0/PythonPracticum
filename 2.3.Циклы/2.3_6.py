a = int(input())
b = int(input())
deliteli_a = []
deliteli_b = []
for x in range(1, a + 1):
    if a % x == 0:
        deliteli_a.append(x)
for y in range(1, b + 1):
    if b % y == 0:
        deliteli_b.append(y)
maxi = []
for i in deliteli_a:
    if i in deliteli_b:
        maxi.append(i)
print(max(maxi))
