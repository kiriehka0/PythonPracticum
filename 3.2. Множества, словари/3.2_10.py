s2 = 'А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Щ Ш Ъ Ь Ы Э Ю Я'
a1 = ['A', 'B', 'V', 'G', 'D', 'E', 'E', 'Zh', 'Z', 'I', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F',
      'Kh', 'Tc', 'Ch', 'Shch', 'Sh', '', '', 'Y', 'E', 'Iu', 'Ia']
a2 = [x for x in s2.split()]
sl = dict(zip(a2, a1))
k = input()
a = []
for x in k:
    if x.upper() not in sl:
        a.append(x)
    else:
        if x == x.upper():
            a.append(sl[x.upper()])
        else:
            a.append(sl[x.upper()].lower())
print("".join(a))
