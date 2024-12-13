def to_string(*args, sep=" ", end="\n"):
    a = []
    for x in args:
        if x != args[-1]:
            a.append(str(x) + sep)
        else:
            a.append(str(x) + end)
    s = ''
    for x in a:
        s = s + x
    return s
