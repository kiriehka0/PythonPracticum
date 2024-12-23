def merge(x, y):
    a1 = 0
    b1 = 0
    a = []
    while (a1 < len(x)) and (b1 < len(y)):
        if y[b1] > x[a1]:
            a.append(x[a1])
            a1 += 1
        else:
            a.append(y[b1])
            b1 += 1
    a += x[a1:]
    a += y[b1:]
    return a


def merge_sort(k):
    if len(k) <= 1:
        return k
    x = k[:len(k) // 2]
    y = k[len(k) // 2:]
    x = merge_sort(x)
    y = merge_sort(y)
    return merge(x, y)
