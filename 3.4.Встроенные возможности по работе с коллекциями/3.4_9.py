from itertools import product, islice
size = int(input())
nums = range(1, size + 1)
table = [x * y for x, y in product(nums, repeat=2)]
for row in range(size):
    print(*islice(table, row * size, (row + 1) * size))
