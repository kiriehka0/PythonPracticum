from itertools import cycle, islice
porridges = [input() for _ in range(int(input()))]
days = int(input())
print('\n'.join(islice(cycle(porridges), days)))
