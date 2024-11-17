from itertools import combinations
names = [input() for _ in range(int(input()))]
print('\n'.join([f'{name1} - {name2}' for name1, name2 in list(combinations(names, 2))]))
