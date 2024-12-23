def answer(x):
    def lalala(*args, **kwargs):
        return f'Результат функции: {x(*args, **kwargs)}'
    return lalala
