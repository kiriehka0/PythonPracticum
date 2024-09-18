pet = int(input())
van = int(input())
tol = int(input())
a = [pet, van, tol]
a.sort(reverse=True)
s = {pet: "Петя", van: "Вася", tol: "Толя"}
print("1.", s[a[0]])
print("2.", s[a[1]])
print("3.", s[a[2]])