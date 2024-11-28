import json
from sys import stdin

n = input()
with open(n, 'r', encoding="utf-8") as f:
    a = json.load(f)
for x in stdin:
    i, y = x.rstrip().split(" == ")
    a[i] = y
with open(n, "w", encoding="UTF-8") as f:
    json.dump(a, f, ensure_ascii=False, indent=4, sort_keys=True)
