s = input()
count = [1] * len(s)
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count[i] = count[i - 1] + 1
for i in range(len(s) - 1):
    if count[i] >= count[i + 1] and i < len(s) - 1:
        print(s[i], count[i], sep=' ')
    elif i == len(s) and count[i] >= count[i + 1]:
        print(s[i], count[i], sep=' ')
        print(s[i + 1], 1)
    elif i == len(s) and count[i] < count[i + 1]:
        print(s[i + 1], count[i] + 1)
print(s[-1], count[-1])
