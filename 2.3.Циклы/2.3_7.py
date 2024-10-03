a = int(input())
b = int(input())
deliteli = []
for s in range(1, 10**9):
    if ((s % a) == 0) and (s % b) == 0:
        deliteli.append(s)
        break
print(deliteli[0])
