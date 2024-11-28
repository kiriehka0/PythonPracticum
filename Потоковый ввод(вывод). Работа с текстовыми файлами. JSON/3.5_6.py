dict = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TC",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ъ": "",
    "Ы": "Y",
    "Ь": "",
    "Э": "E",
    "Ю": "IU",
    "Я": "IA",
}
a = []
b = []
with open("cyrillic.txt", "r", encoding="utf-8") as f:
    for x in f:
        a.append(x.rstrip("\n"))
for x in a:
    s = ""
    for i in x:
        if i.upper() in dict.keys():
            if i.upper() == i:
                s += dict[i].lower().capitalize()
            else:
                s += dict[i.upper()].lower()
        else:
            s = s + i
    b.append(s)
with open("transliteration.txt", "w", encoding="UTF-8") as f1:
    print(*b, sep="\n", file=f1)
