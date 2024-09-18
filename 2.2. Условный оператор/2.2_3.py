pet = int(input())
van = int(input())
tol = int(input())
a = [pet, van, tol]
a.sort()
if a[2] == tol:
    print("Толя")
if a[2] == van:
    print("Вася")
if a[2] == pet:
    print("Петя")