from math import factorial
s = s1 = (input()).split()
step = 0
for i in range(len(s1)):
    if s1[i] in '+-*~/!#@':
        if s[i - step] == '*':
            s[i - step] = str(int(s[i - 2 - step]) * int(s[i - 1 - step]))
            s = s[:i - 2 - step] + s[i - step:]
            step += 2
        elif s[i - step] == '-':
            s[i - step] = str(int(s[i - 2 - step]) - int(s[i - 1 - step]))
            s = s[:i - 2 - step] + s[i - step:]
            step += 2
        elif s[i - step] == '+':
            s[i - step] = str(int(s[i - 2 - step]) + int(s[i - 1 - step]))
            s = s[:i - 2 - step] + s[i - step:]
            step += 2
        elif s[i - step] == '/':
            s[i - step] = str(int(s[i - 2 - step]) // int(s[i - 1 - step]))
            s = s[:i - 2 - step] + s[i - step:]
            step += 2
        elif s[i - step] == '~':
            s[i - step] = str(int(s[i - 1 - step]) * (-1))
            s = s[:i - 1 - step] + s[i - step:]
            step += 1
        elif s[i - step] == '!':
            s[i - step] = str(factorial(int(s[i - 1 - step])))
            s = s[:i - 1 - step] + s[i - step:]
            step += 1
        elif s[i - step] == '#':
            s[i - step] = s[i - 1 - step]
        elif s[i - step] == '@':
            s[i - step - 3], s[i - step - 2], s[i - step - 1] = s[i - step - 2], s[i - step - 1], s[i - step - 3]
            s = s[:i - step] + s[i + 1 - step:]
            step += 1
    else:
        ...
print(*s)
