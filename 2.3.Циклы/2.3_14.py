a = int(input())
deliteli = [a]
for i in range(1, round(a ** 0.5) + 1):
    if a % i == 0:
        deliteli.append(i)
if a == 1:
    print("NO")
else:
    if len(deliteli) == 2:
        print("YES")
    else:
        print("NO")
