s = []


def modern_print(x):
    if x not in s:
        s.append(x)
        print(x)
