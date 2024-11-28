a = int(input())
s = ""
with open("public.txt", "r", encoding="UTF-8") as f:
    b = f.read()
    for x in b:
        if 65 <= ord(x) <= 90:
            s += chr(65 + (ord(x) - 65 + a) % (90 - 65 + 1))
        elif 97 <= ord(x) <= 122:
            s += chr(97 + (ord(x) - 97 + a) % (122 - 97 + 1))
        else:
            s += x

with open("private.txt", "w") as f1:
    f1.write(s)
