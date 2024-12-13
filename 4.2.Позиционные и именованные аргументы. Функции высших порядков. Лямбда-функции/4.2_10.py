def secret_replace(text, **replaces):
    replaces = {x: [y, 0] for x, y in replaces.items()}
    a = ""
    for x in text:
        if x in replaces:
            y = replaces[x][1] % len(replaces[x][0])
            replaces[x] = [replaces[x][0], y + 1]
            a += replaces[x][0][y]
        else:
            a += x
    return a
