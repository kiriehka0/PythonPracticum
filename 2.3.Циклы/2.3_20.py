last_h = 0
for i in range(int(input())):
    block = int(input())
    now_h = block % 256
    r = (block // 256) % 256
    m = block // 256 ** 2
    calc_h = (37 * (m + r + last_h)) % 256
    if calc_h != now_h or calc_h > 100:
        print(i)
        break
    last_h = calc_h
else:
    print(-1)
