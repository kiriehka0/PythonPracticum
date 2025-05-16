import requests
from functools import reduce

# URL сервера
url = "http://127.0.0.1:5000/"

# Множество для хранения уникальных ответов сервера
unique_responses = set()

# Собираем все уникальные ответы сервера
while True:
    response = requests.get(url).json()  # Получаем JSON-ответ
    # Преобразуем список в кортеж (так как списки нехешируемы) для добавления в множество
    response_tuple = tuple(sorted(response))
    if response_tuple in unique_responses:
        break  # Прекращаем, если ответ уже встречался
    unique_responses.add(response_tuple)

# Преобразуем кортежи обратно в списки
responses = [list(resp) for resp in unique_responses]

# Находим пересечение всех списков
common_elements = set(responses[0])
for lst in responses[1:]:
    common_elements.intersection_update(lst)

# Сортируем результат без учёта регистра
sorted_result = sorted(common_elements, key=lambda x: x.lower())

# Выводим результат
for item in sorted_result:
    print(item)
