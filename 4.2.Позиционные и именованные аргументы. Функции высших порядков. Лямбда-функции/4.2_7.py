a = []
x = []
b = []


def enter_results(*args):
    global a, x, b
    a.extend(list(args))
    x = a[::2]
    b = a[1::2]


def get_average():
    return round(sum(x) / len(x), 2), round(sum(b) / len(b), 2)


def get_sum():
    return round(sum(x), 2), round(sum(b), 2)
