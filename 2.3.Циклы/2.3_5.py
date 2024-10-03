a = float(input())
sum = 0
while a != 0:
    if a >= 500:
        sum = sum + a - (a * 0.1)
    else:
        sum = sum + a
    a = float(input())
print(sum)
