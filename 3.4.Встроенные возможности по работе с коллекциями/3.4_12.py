string = []
for _ in range(int(input())):
    string.extend(input().split(', '))
lst = enumerate(sorted(string), 1)
print('\n'.join([f'{num}. {item}' for num, item in lst]))
