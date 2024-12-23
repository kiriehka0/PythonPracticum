def result_accumulator(x):
    a = []

    def wrapper(*args, method='accumulate', **kwargs):
        a.append(x(*args, **kwargs))
        if method == 'drop':
            b = list(a)
            a.clear()
            return b

    return wrapper
