def make_equation(*args):
    if len(args) == 1:
        return f'{args[0]}'
    else:
        return f'({make_equation(*args[:-1])}) * x + {args[-1]}'
