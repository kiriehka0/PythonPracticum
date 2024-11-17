from itertools import product
num = int(input())
nums = range(1, num - 1)
table = list(product(nums, repeat=3))
print('А Б В')
for i in range(len(table)):
    if sum(table[i]) == num:
        print(*table[i])
