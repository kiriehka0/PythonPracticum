name = input()
sena = int(input())
ves = int(input())
money = int(input())
k = f"{name}"
k1 = k.rjust(28, " ")
k2 = f"{ves}кг * {sena}руб/кг"
k3 = k2.rjust(29, " ")
s = f"{ves * sena}руб"
s1 = s.rjust(28, " ")
h = f"{money}руб"
h1 = h.rjust(26, " ")
g = f"{money - (ves * sena)}руб"
g1 = g.rjust(28, " ")
print("================Чек================")
print("Товар:", k1)
print("Цена:", k3)
print("Итого:", s1)
print("Внесено:", h1)
print("Сдача:", g1)
print("=" * 35)
