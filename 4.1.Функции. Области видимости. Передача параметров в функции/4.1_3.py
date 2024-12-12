def number_length(x):
    if str(x)[0] != '-' and str(x)[0] != '+':
        return len(str(x))
    if str(x)[0] == '-' or str(x)[0] == '+':
        return len(str(x)[1:])
