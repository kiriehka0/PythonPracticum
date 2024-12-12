def make_matrix(x, y=0):
    if isinstance(x, int):
        s = [[y] * x for i in range(x)]
        return s
    else:
        s = [[y] * x[0] for i in range(x[1])]
        return s


