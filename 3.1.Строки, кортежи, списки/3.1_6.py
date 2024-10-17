n = int(input())
cnt = 0
for x in range(n):
    k = input()
    cnt += k.count('зайка')
print(cnt)
