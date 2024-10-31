k = int(input())
cnt = 0
a1 = [input() for x in range(k)]
b = [[x, a1.count(x)] for x in set(a1) if a1.count(x) > 1]
if len(b) == 0:
    print('Однофамильцев нет')
else:
    for x, y in sorted(b):
        print(f"{x} - {y}")
