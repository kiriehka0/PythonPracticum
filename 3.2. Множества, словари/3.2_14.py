n = int(input())
pop = []
sast = []
for x in range(n):
    ingredienti = input()
    pop.append(ingredienti)
n2 = int(input())
for x in range(n2):
    bludo = input()
    a = []
    k = []
    kolvo = int(input())
    for y in range(kolvo):
        ingredient = input()
        a.append(ingredient)
    for x1 in a:
        if x1 in pop:
            k.append(x1)
    if len(k) == kolvo:
        sast.append(bludo)
if len(sast) == 0:
    print('Готовить нечего')
else:
    for x in sorted(sast):
        print(x)
