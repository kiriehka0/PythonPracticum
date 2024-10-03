x = 0
y = 0
a = input()
a1 = int(input())
while a != "СТОП":
    if a == "СЕВЕР":
        x += a1
    if a == "ЮГ":
        x -= a1
    if a == "ЗАПАД":
        y -= a1
    if a == "ВОСТОК":
        y += a1
    a = input()
    if a == "СТОП":
        break
    a1 = int(input())
print(x)
print(y)
