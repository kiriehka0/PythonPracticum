from itertools import count
start, stop, step = [float(x) for x in input().split()]
for num in count(start, step):
    if num >= stop:
        break
    print(f'{num:.2f}')
