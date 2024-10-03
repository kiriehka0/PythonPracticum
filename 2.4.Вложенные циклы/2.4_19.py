n = int(input())
k = len(str((n + 1) // 2))
for i in range(n):
    for x in range(n):
        print(f"{min(i + 1, x + 1, n - i, n - x):>{k}}", end=" ")
    print()
