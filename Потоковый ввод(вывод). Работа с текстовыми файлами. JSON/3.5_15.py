from sys import stdin

a = input().lower()
a1 = False
b = [line.strip() for line in stdin]
for x in b:
    with open(x, "r", encoding="UTF-8") as f:
        f1 = f.read()
        f1 = ' '.join(f1.lower().split())
        if a in f1:
            a1 = True
            print(x)
if a1 is False:
    print("404. Not Found")
