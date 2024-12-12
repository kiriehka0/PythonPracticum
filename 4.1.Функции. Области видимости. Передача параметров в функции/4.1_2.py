def gcd(x, y):
    deliteli1 = [i for i in range(1, x + 1) if x % i == 0]
    deliteli2 = [i for i in range(1, y + 1) if y % i == 0]
    maxi = [x for x in deliteli1[::-1] for y in deliteli2[::-1] if x == y]
    return maxi[0]
