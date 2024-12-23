def make_linear(x):
    a = []
    for i in x:
        if isinstance(i, list):
            a.extend(make_linear(i))
        else:
            a.append(i)
    return a
