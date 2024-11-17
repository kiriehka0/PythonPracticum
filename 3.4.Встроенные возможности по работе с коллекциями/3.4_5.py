from itertools import chain
lst = sorted(set(chain.from_iterable([input().split(", ") for _ in range(3)])))
for index, value in enumerate(lst, 1):
    print(f"{index}. {value}")
