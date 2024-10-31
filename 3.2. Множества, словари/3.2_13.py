n = int(input())
bluda = [input() for x in range(n)]
n2 = int(input())
nedela = []
for x in range(n2):
    a1 = int(input())
    den = [input() for i in range(a1)]
    nedela.append(den)
for x in nedela:
    for x1 in x:
        if x1 in bluda:
            bluda.remove(x1)
if len(bluda) == 0:
    print("Готовить нечего")
else:
    for x in sorted(bluda):
        print(x)
