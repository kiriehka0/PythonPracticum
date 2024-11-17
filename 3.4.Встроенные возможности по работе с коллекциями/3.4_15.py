from itertools import permutations
lst = []
for _ in range(num := int(input())):
    lst.extend(input().split(', '))
lst.sort()
for items in permutations(lst, 3):
    print(' '.join(items))
