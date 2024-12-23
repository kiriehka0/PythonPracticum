def same_type(x):
    def op(*args):
        if len({type(x) for x in args}) > 1:
            print('Обнаружены различные типы данных')
            return False
        return x(*args)

    return op
