def month(month_number, language_code):
    month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    months_russian = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                      "Ноябрь", "Декабрь"]
    months_english = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]

    russian_months_dict = dict(zip(month_numbers, months_russian))
    english_months_dict = dict(zip(month_numbers, months_english))

    if language_code == "ru":
        return russian_months_dict[month_number]
    elif language_code == "en":
        return english_months_dict[month_number]
    else:
        return None
