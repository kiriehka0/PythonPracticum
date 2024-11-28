a = input()
n = int(input())
with open(a, "r", encoding="utf-8") as f:
    print(*f.readlines()[-n:], sep="")
