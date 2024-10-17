s = (input()).lower().replace(' ', '')
length = len(s) // 2
if len(s) % 2 == 0 and s[:length] == s[length:][::-1]:
    print('YES')
elif len(s) % 2 != 0 and s[:length] == s[(length + 1):][::-1]:
    print('YES')
else:
    print('NO')
