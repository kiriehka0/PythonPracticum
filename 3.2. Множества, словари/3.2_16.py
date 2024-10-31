objects = set()
while (s := input()) != '':
    z = s.split()
    for i in range(len(z)):
        if i == 0 and z[i] == 'зайка':
            objects.add(z[i + 1])
        elif i == len(z) - 1 and z[i] == 'зайка':
            objects.add(z[i - 1])
        elif z[i] == 'зайка':
            objects.add(z[i - 1])
            objects.add(z[i + 1])
print(*objects, sep='\n')
