n = int(input())
a1 = []
for i in range(n):
    packet = input().strip()
    a, b, s = packet.split('&')
    a = int(a)
    b = int(b)
    s1 = s[a:]
    s2 = s1[::2]
    res = s2[:b]
    a1.append(res)
for x in a1:
    print(x)
