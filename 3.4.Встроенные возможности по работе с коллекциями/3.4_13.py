from itertools import permutations
names = []
for _ in range(num := int(input())):
    names.append(input())
names.sort()
for name_list in permutations(names, num):
    print(', '.join(name_list))
