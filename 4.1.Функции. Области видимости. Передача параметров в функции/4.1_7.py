def can_eat(x, y):
    if ((x[0] - 1 == y[0] and x[1] + 2 == y[1]) or (
            x[0] - 2 == y[0] and x[1] + 1 == y[1]) or (x[0] + 1 == y[0] and x[1] + 2 == y[1]) or (
            x[0] - 2 == y[0] and x[1] - 1 == y[1]) or (x[0] - 1 == y[0] and x[1] - 2 == y[1]) or (
            x[0] + 2 == y[0] and x[1] - 1 == y[1]) or (x[0] + 1 == y[0] and x[1] - 2 == y[1]) or (
            x[0] + 2 == y[0] and x[1] + 1 == y[1])):
        return True
    else:
        return False
