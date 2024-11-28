import os
import math

a = os.path.dirname(__file__)
b = input()
c = os.path.getsize(a + "/" + b)
spisok = ["Б", "КБ", "МБ", "ГБ"]
index = 0
while c >= 1024 and index < len(spisok) - 1:
    c = math.ceil(c / 1024)
    index += 1
print(c, spisok[index], sep="")
