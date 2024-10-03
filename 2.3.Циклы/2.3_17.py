a = int(input())
k = [int(x) for x in str(a)]
b = k.copy()
for i in b:
    if i % 2 == 0:
        k.remove(i)
s = ""
for x in k:
    s = s + str(x)
print(s)
