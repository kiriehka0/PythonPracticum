year = int(input())
a = [int(x) for x in range(0, 10000, 4)]
a.remove(1700)
a.remove(1800)
a.remove(1900)
a.remove(2100)
a.remove(2200)
a.remove(2300)
if year in a:
    print("YES")
else:
    print("NO")