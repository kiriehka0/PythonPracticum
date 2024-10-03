n = 500
d = n // 2
print(n)
while (answer := input()) != 'Угадал!':
    if answer == 'Меньше':
        n = n - d
    if answer == 'Больше':
        n = n + d
    if d >= 2:
        d = (d + 1) // 2
    print(n)
