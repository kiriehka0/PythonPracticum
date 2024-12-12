def is_prime(y):
    a = True
    for x in range(2, round(y ** (0.5))):
        if y % x == 0:
            a = False
    return a


