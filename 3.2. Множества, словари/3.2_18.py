kolvo = {}
for _ in range(int(input())):https://lms.yandex.ru/courses/1217/groups/35771/lessons/7482/tasks/56822
    x = input().split()
    if not (cord := f'{x[0][:-1]}-{x[1][:-1]}') in kolvo:
        kolvo[cord] = 1
    else:
        kolvo[cord] += 1
print(max(kolvo.values()))
