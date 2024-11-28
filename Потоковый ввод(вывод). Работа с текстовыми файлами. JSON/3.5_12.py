from sys import stdin
n = input()
n1 = input()
n3 = input()
n4 = input()
with open(n, "r", encoding="utf-8") as f:
    for x in f:
        a, a1, a2 = [], [], []
        for i in x.split():
            cnt = sum([i.count(str(x)) for x in range(0, 9, 2)])
            cnt2 = sum([i.count(str(x)) for x in range(1, 10, 2)])
            if cnt > cnt2:
                a.append(i)
            elif cnt < cnt2:
                a1.append(i)
            else:
                a2.append(i)
        for x, y in zip(
            [n1, n3, n4],
            [a, a1, a2],
        ):
            with open(x, "a", encoding="UTF-8") as f:
                print(*y, file=f)
