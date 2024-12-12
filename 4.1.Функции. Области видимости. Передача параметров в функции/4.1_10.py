def merge(x, y):
    s = []
    for i in x:
        s.append(i)
    for i in y:
        s.append(i)
    s2 = []
    h = len(s)
    while len(s2) != h:
        mini = 10000
        for x in s:
            if x < mini:
                mini = x
        s.remove(mini)
        s2.append(mini)
    return tuple(s2)
