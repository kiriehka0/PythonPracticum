n = int(input())
a = []
for i in range(n):
    k = input()
    a.append(k[0])
cnt = 0
for x in a:
    if x == 'а' or x == "б" or x == "в":
        cnt += 1
if cnt == len(a):
    print('YES')
else:
    print("NO")
