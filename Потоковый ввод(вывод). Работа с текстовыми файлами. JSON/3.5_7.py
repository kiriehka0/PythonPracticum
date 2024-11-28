with open(input(), mode='r', encoding='utf-8') as f:
    a = list(map(int, f.read().split()))
    print(len(a))
    print(len([x for x in a if x > 0]))
    print(min(a))
    print(max(a))
    print(sum(a))
    print(round((sum(a) / len(a)), 2))
