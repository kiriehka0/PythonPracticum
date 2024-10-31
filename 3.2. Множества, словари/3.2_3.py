k = []
for x in range(n := int(input())):
    s = input().split()
    for x in s:
        k.append(x)
for x in set(k):
    print(x)
