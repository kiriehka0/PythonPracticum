with open("secret.txt", "r", encoding="UTF-8") as f:
    f1 = f.read()
    for x in f1:
        print(chr(ord(x) % 128), end="")
