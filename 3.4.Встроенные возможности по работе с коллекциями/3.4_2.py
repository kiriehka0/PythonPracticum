left = input().split(', ')
right = input().split(', ')
for kids in zip(left, right):
    print(f'{kids[0]} - {kids[1]}')
