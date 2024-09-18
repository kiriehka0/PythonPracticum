a = int(input())
b = int(input())
c = int(input())
if ((a ** 2) + (b ** 2) == (c ** 2)) or ((a ** 2) + (c ** 2) == (b ** 2)) or ((c ** 2) + (b ** 2) == (a ** 2)):
    print("100%")
k = max(a, b, c)
if (k ** 2) > ((min(a, b, c) ** 2) + ((a + b + c - max(a, b, c) - min(a, b, c)) ** 2)):
    print("велика")
if (k ** 2) < ((min(a, b, c) ** 2) + ((a + b + c - max(a, b, c) - min(a, b, c)) ** 2)):
    print("крайне мала")
