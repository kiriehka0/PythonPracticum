from itertools import permutations
str = []
for _ in range(num := int(input())):
    str.append(input())
str.sort()
for pos in permutations(str, 3):
    print(', '.join(pos))
