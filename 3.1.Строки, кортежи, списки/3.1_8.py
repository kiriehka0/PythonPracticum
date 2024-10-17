n = int(input())
a = []
for x in range(n):
    k = input()
    if 'зайка' in k:
        a.append(k.index('зайка') + 1)
    else:
        a.append('Заек нет =(')
for x in a:
    print(x)
