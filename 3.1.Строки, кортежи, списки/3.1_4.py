k = input()
a = []
while k != '':
    if k[-1] != '@' and k[-2] != '@' and k[-3] != '@':
        if k[0] == '#' and k[1] == '#':
            a.append(k[2:])
        else:
            a.append(k)
    k = input()
for x in a:
    print(x)
