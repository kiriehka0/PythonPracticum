{
    x: text.lower().count(x)
    for x in "".join(text.lower().split())
    if x in "абвгдеёжзиклмнопрстуфхцшщъыьэюяabcdefghijklmnopqrstuvwxyz"
}
