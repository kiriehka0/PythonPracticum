s = s1 = (input()).split()
step = 0
for i in range(len(s1)):
    if s1[i] in '+-*':
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
    else:
        ...
print(*s)
