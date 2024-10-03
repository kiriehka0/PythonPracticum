c = input()
cnt = 0
while c != "Приехали!":
    if "зайка" in c:
        cnt += 1
    c = input()
print(cnt)
