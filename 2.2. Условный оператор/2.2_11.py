a = int(input())
a = str(a)
k = [int(a[0]), int(a[1]), int(a[2])]
maxi = max(k)
mini = min(k)
if maxi + mini == (sum(k) - maxi - mini) * 2:
    print("YES")
else:
    print("NO")
