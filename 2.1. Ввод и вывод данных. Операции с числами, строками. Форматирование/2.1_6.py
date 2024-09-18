name = input()
sena = int(input())
ves = int(input())
money = int(input())
k = ves * sena
sdaha = money - k
print("Чек")
print(f"{name} - {ves}кг - {sena}руб/кг")
print(f"Итого: {k}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {sdaha}руб")