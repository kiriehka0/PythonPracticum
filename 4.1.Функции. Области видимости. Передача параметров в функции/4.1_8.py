def is_palindrome(x):
    if isinstance(x, int):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
    if isinstance(x, str):
        if x == x[::-1]:
            return True
        else:
            return False
    if isinstance(x, tuple):
        a = list(x)
        b = a[::-1]
        if a == b:
            return True
        else:
            return False
    if isinstance(x, list):
        if x == x[::-1]:
            return True
        else:
            return False
