cnt = int(input())
a = 3
for i in range(1, cnt + 1):
    for x in range(a):
        print('До старта', a - x, 'секунд(ы)')
    print(f'Старт {i}!!!')
    a += 1
