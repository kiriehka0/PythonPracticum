a = int(input())
b = input()
cnt = 1
k = []
k.append(b)
while cnt != a:
    cnt += 1
    b = input()
    k.append(b)
print(min(k))
