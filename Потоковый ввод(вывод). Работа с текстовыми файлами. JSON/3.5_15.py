import json
from sys import stdin

a = [x.rstrip() for x in stdin]
with open("scoring.json", "r", encoding="UTF-8") as f:
    data = json.load(f)
spisok = []
for x in data:
    b = x["points"] // len(x["tests"])
    for y in x["tests"]:
        spisok.append((y["pattern"], b))
if len(a) != len(spisok):
    print("Неверное количество выходных строк")
else:
    cnt = 0
    for i in range(len(spisok)):
        hoh = a[i]
        hoh1 = spisok[i][0]
        lala = spisok[i][1]
        if hoh == hoh1:
            cnt += lala
    print(cnt)
