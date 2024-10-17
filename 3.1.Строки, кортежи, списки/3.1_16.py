phrases = []
length = int(input())
summary_len = 0
step = 0
for i in range(n := int(input())):
    phrases.append(phrase := input())
for i in range(len(phrases)):
    if summary_len == length or phrases[i - step] == '':
        del phrases[i - step]
        step += 1
    elif len(phrases[i - step]) < length - 3 - summary_len:
        summary_len += len(phrases[i - step])
    elif len(phrases[i - step]) == length - 3 - summary_len:
        phrases[i - step] += '...'
        summary_len = length
    elif len(phrases[i - step]) > length - 3 - summary_len:
        phrases[i - step] = phrases[i - step][:length - 3 - summary_len] + '...'
        summary_len = length
print(*phrases, sep='\n')
