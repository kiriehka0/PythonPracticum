n = input()
s = n.split()
k = int(input())
for x in s:
    print(str(int(x)**k), end=' ')
