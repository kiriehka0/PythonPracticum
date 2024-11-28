import json

n = input()
n2 = input()
a = []
with open(n, "r", encoding="UTF-8") as f:
    for line in f:
        a += [int(x) for x in line.split()]
dict = {
    "count": len(a),
    "positive_count": len([x for x in a if x > 0]),
    "min": min(a),
    "max": max(a),
    "sum": sum(a),
    "average": round((sum(a) / len(a)), 2),
}
with open(n2, "w", encoding="UTF-8") as f1:
    json.dump(dict, f1, ensure_ascii=False, indent=4)
