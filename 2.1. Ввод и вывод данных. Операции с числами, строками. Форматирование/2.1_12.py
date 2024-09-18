a = int(input())
b = int(input())
if len(str(a)) == 2:
    a1 = str(a)[0]
    a2 = str(a)[1]
    k = 0
if len(str(a)) == 3:
    a1 = str(a)[0]
    a2 = str(a)[1]
    a3 = str(a)[2]
    k = 1
if len(str(b)) == 2:
    b1 = str(b)[0]
    b2 = str(b)[1]
    k1 = 0
if len(str(b)) == 3:
    b1 = str(b)[0]
    b2 = str(b)[1]
    b3 = str(b)[2]
    k1 = 1
if k == 0 and k1 == 0:
    print(str((int(a1) + int(b1)) % 10) + str(((int(a2) + int(b2)) % 10)))
if k == 1 and k1 == 1:
    print(str((int(a1) + int(b1)) % 10) + str((int(a2) + int(b2)) % 10) + str((int(a3) + int(b3)) % 10))
if k == 0 and k1 == 1:
    print(str(b1) + str((int(a1) + int(b2)) % 10) + str((int(a2) + int(b3)) % 10))
if k == 1 and k1 == 0:
    print(str(a1) + str((int(a2) + int(b1)) % 10) + str((int(a3) + int(b2)) % 10))