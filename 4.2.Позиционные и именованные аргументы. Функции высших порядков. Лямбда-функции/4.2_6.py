drink = {"Капучино": (1, 3, 0), "Эспрессо": (1, 0, 0), "Макиато": (2, 1, 0), "Кофе по-венски": (1, 0, 2),
         "Латте Макиато": (1, 2, 1), "Кон Панна": (1, 0, 1)}
in_stock = {}


def order(*drinks):
    global in_stock
    global drink
    a = []
    for x in drinks:
        if drink[x][0] <= in_stock["coffee"] and drink[x][1] <= in_stock["milk"] and drink[x][2] <= \
                in_stock["cream"]:
            a.append(x)
            in_stock["coffee"] -= drink[x][0]
            in_stock["milk"] -= drink[x][1]
            in_stock["cream"] -= drink[x][2]
            return x
    if len(a) == 0:
        return "К сожалению, не можем предложить Вам напиток"
